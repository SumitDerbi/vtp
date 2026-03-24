#!/bin/bash

#===============================================================================
# First-Time Setup Script for cPanel Python Application — VTP
# Usage: ./deployment_first_time.sh [branch_name] [env_name]
# Example: ./deployment_first_time.sh main vtp
#
# This script runs the FULL deployment + first-time-only tasks:
#   - setup_pages (create Wagtail page tree)
#   - createsuperuser
#
# After first-time setup, use deployment.sh for subsequent deploys.
#===============================================================================

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
DEFAULT_BRANCH="main"
DEFAULT_ENV_NAME="vtp"
DEPLOY_CONFIG_BASE="$HOME/deploy_config"

# Parse arguments
BRANCH="${1:-$DEFAULT_BRANCH}"
ENV_NAME="${2:-$DEFAULT_ENV_NAME}"

# Build paths from environment name
CONFIG_PATH="${DEPLOY_CONFIG_BASE}/${ENV_NAME}/${ENV_NAME}.config"
ENV_FILE_PATH="${DEPLOY_CONFIG_BASE}/${ENV_NAME}/${ENV_NAME}.env"

#===============================================================================
# Helper Functions
#===============================================================================

log_info() {
    echo -e "${BLUE}[INFO]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

cleanup_on_error() {
    log_error "First-time setup failed!"
    if [ -n "${BACKUP_DIR:-}" ] && [ -d "$BACKUP_DIR" ]; then
        log_warn "A backup exists at: $BACKUP_DIR"
    fi
    exit 1
}

trap cleanup_on_error ERR

#===============================================================================
# Load Configuration
#===============================================================================

load_config() {
    if [ ! -f "$CONFIG_PATH" ]; then
        log_error "Config file not found at: $CONFIG_PATH"
        log_info "Expected location: ~/deploy_config/<env_name>/<env_name>.config"
        log_info "Please create a config file with the following variables:"
        cat <<EOF
# ${ENV_NAME}.config - Sample Configuration
GIT_DIR=~/repositories/${ENV_NAME}
APP_DIR=~/${ENV_NAME}
VIRTUALENV_PATH=~/virtualenv/${ENV_NAME}/3.11/
ACTIVATE_ENV=~/virtualenv/${ENV_NAME}/3.11/bin/activate
DB_BACKUP_PATH=~/backups/${ENV_NAME}/
STATIC_ROOT=~/${ENV_NAME}/staticfiles/
ENV_FILE=~/deploy_config/${ENV_NAME}/${ENV_NAME}.env
CONFIG_FILE=~/deploy_config/${ENV_NAME}/${ENV_NAME}.config
REQUIREMENTS_FILE=requirements/production.txt
DOMAIN_DOC_ROOT=~/yourdomain.com
EOF
        exit 1
    fi

    log_info "Loading configuration from: $CONFIG_PATH"

    CONFIG_CONTENT=$(cat "$CONFIG_PATH" | tr -d '\r')
    eval "$CONFIG_CONTENT"

    ENV_FILE="${ENV_FILE:-$ENV_FILE_PATH}"

    local required_vars=(
        "GIT_DIR"
        "APP_DIR"
        "VIRTUALENV_PATH"
        "ACTIVATE_ENV"
        "REQUIREMENTS_FILE"
    )

    for var in "${required_vars[@]}"; do
        if [ -z "${!var:-}" ]; then
            log_error "Required variable '$var' is not set in config file."
            exit 1
        fi
    done

    GIT_DIR=$(eval echo "$GIT_DIR" | sed 's:/*$::')
    APP_DIR=$(eval echo "$APP_DIR" | sed 's:/*$::')
    VIRTUALENV_PATH=$(eval echo "$VIRTUALENV_PATH" | sed 's:/*$::')
    ACTIVATE_ENV=$(eval echo "$ACTIVATE_ENV")
    DB_BACKUP_PATH=$(eval echo "${DB_BACKUP_PATH:-~/backups/}" | sed 's:/*$::')
    STATIC_ROOT=$(eval echo "${STATIC_ROOT:-}" | sed 's:/*$::')
    ENV_FILE=$(eval echo "${ENV_FILE:-}")
    CONFIG_FILE=$(eval echo "${CONFIG_FILE:-}")

    log_success "Configuration loaded successfully."
}

#===============================================================================
# Pre-flight Checks
#===============================================================================

preflight_checks() {
    log_info "Running pre-flight checks..."

    if ! command -v git &>/dev/null; then
        log_error "git is not installed or not in PATH."
        exit 1
    fi

    if [ ! -d "$GIT_DIR" ]; then
        log_error "Git repository not found at: $GIT_DIR"
        exit 1
    fi

    if [ ! -d "$GIT_DIR/.git" ]; then
        log_warn "Directory exists but is not a git repository: $GIT_DIR"
    else
        log_info "Git repository verified at: $GIT_DIR"
    fi

    if [ ! -f "$ACTIVATE_ENV" ]; then
        log_error "Virtual environment not found at: $ACTIVATE_ENV"
        log_info "Please create the virtual environment first via cPanel > Setup Python App."
        exit 1
    fi

    if [ -n "$ENV_FILE" ] && [ ! -f "$ENV_FILE" ]; then
        log_warn "Environment file not found at: $ENV_FILE (skipping .env copy)"
    fi

    log_success "Pre-flight checks passed."
}

#===============================================================================
# Pull Latest Code
#===============================================================================

pull_latest_code() {
    log_info "Pulling latest code from branch: $BRANCH"

    cd "$GIT_DIR"
    git fetch --all

    if ! git branch -a | grep -qE "(^|\s)remotes/origin/${BRANCH}$"; then
        log_error "Branch '$BRANCH' does not exist on remote."
        git branch -a
        exit 1
    fi

    git checkout "$BRANCH"
    git reset --hard "origin/$BRANCH"
    git pull origin "$BRANCH"

    LATEST_COMMIT=$(git log -1 --pretty=format:"%h - %s (%ci)")
    log_success "Code updated to: $LATEST_COMMIT"
}

#===============================================================================
# Sync Code to App Directory
#===============================================================================

sync_code() {
    log_info "Syncing code to application directory: $APP_DIR"

    mkdir -p "$APP_DIR"

    rsync -av --delete \
        --exclude='.git' \
        --exclude='.gitignore' \
        --exclude='__pycache__' \
        --exclude='*.pyc' \
        --exclude='.env' \
        --exclude='.htaccess' \
        --exclude='db.sqlite3' \
        --exclude='media/' \
        --exclude='node_modules/' \
        --exclude='.vscode/' \
        --exclude='.idea/' \
        --exclude='staticfiles/' \
        --exclude='logs/' \
        --exclude='cache/' \
        --exclude='plan/' \
        --exclude='doc/' \
        "$GIT_DIR/" "$APP_DIR/"

    chmod 711 "$APP_DIR"

    log_success "Code synced successfully."
}

#===============================================================================
# Copy Environment & Config Files
#===============================================================================

copy_env_files() {
    log_info "Copying environment and config files..."

    if [ -n "$ENV_FILE" ] && [ -f "$ENV_FILE" ]; then
        cp "$ENV_FILE" "$APP_DIR/.env"
        # Strip Windows carriage returns (\r) to avoid parsing errors on Linux
        sed -i 's/\r$//' "$APP_DIR/.env"
        log_success "Environment file copied: $ENV_FILE -> $APP_DIR/.env"
    fi

    if [ -n "${CONFIG_FILE:-}" ] && [ -f "$CONFIG_FILE" ]; then
        CONFIG_BASENAME=$(basename "$CONFIG_FILE")
        cp "$CONFIG_FILE" "$APP_DIR/$CONFIG_BASENAME"
        log_success "Config file copied: $CONFIG_FILE -> $APP_DIR/$CONFIG_BASENAME"
    fi
}

#===============================================================================
# Install Dependencies
#===============================================================================

install_dependencies() {
    log_info "Installing Python dependencies..."

    source "$ACTIVATE_ENV"
    export DJANGO_SETTINGS_MODULE="vtp.settings.production"
    log_info "Virtual environment activated: $(which python)"
    log_info "Python version: $(python --version)"

    cd "$APP_DIR"

    pip install --upgrade pip

    if [ -f "$APP_DIR/$REQUIREMENTS_FILE" ]; then
        pip install -r "$APP_DIR/$REQUIREMENTS_FILE"
        log_success "Dependencies installed from: $REQUIREMENTS_FILE"
    else
        log_warn "Requirements file not found: $APP_DIR/$REQUIREMENTS_FILE (skipping)"
    fi
}

#===============================================================================
# Run Migrations
#===============================================================================

run_migrations() {
    log_info "Running database migrations..."

    cd "$APP_DIR"
    source "$ACTIVATE_ENV"
    export DJANGO_SETTINGS_MODULE="vtp.settings.production"

    # Load .env variables into the shell
    if [ -f "$APP_DIR/.env" ]; then
        set -a
        source "$APP_DIR/.env"
        set +a
    fi

    if [ -f "$APP_DIR/manage.py" ]; then
        python manage.py migrate --noinput
        log_success "Database migrations completed."
    else
        log_warn "manage.py not found. Skipping migrations."
    fi
}

#===============================================================================
# First-Time: Create Superuser
#===============================================================================

create_superuser() {
    log_info "Creating superuser..."

    cd "$APP_DIR"
    source "$ACTIVATE_ENV"
    export DJANGO_SETTINGS_MODULE="vtp.settings.production"

    # Load .env variables into the shell
    if [ -f "$APP_DIR/.env" ]; then
        set -a
        source "$APP_DIR/.env"
        set +a
    fi

    if [ -f "$APP_DIR/manage.py" ]; then
        python manage.py createsuperuser
        log_success "Superuser created."
    fi
}

#===============================================================================
# First-Time: Setup Default Pages
#===============================================================================

setup_pages() {
    log_info "Setting up default Wagtail page tree..."

    cd "$APP_DIR"
    source "$ACTIVATE_ENV"
    export DJANGO_SETTINGS_MODULE="vtp.settings.production"

    # Load .env variables into the shell
    if [ -f "$APP_DIR/.env" ]; then
        set -a
        source "$APP_DIR/.env"
        set +a
    fi

    if [ -f "$APP_DIR/manage.py" ]; then
        python manage.py setup_pages
        log_success "Default pages created."
    fi
}

#===============================================================================
# Collect Static Files
#===============================================================================

collect_static() {
    log_info "Collecting static files..."

    cd "$APP_DIR"
    source "$ACTIVATE_ENV"
    export DJANGO_SETTINGS_MODULE="vtp.settings.production"

    # Load .env variables into the shell
    if [ -f "$APP_DIR/.env" ]; then
        set -a
        source "$APP_DIR/.env"
        set +a
    fi

    if [ -f "$APP_DIR/manage.py" ]; then
        if [ -n "$STATIC_ROOT" ]; then
            python manage.py collectstatic --noinput
            log_success "Static files collected to: $STATIC_ROOT"
        else
            log_warn "STATIC_ROOT not set. Skipping collectstatic."
        fi
    fi
}

#===============================================================================
# Create Symlinks for Media & Static
#===============================================================================

create_symlinks() {
    log_info "Creating symlinks for media and static files..."

    DOMAIN_DOC_ROOT=$(eval echo "${DOMAIN_DOC_ROOT:-}")

    if [ -z "$DOMAIN_DOC_ROOT" ]; then
        log_warn "DOMAIN_DOC_ROOT not set in config — skipping symlinks."
        return
    fi

    if [ ! -d "$DOMAIN_DOC_ROOT" ]; then
        log_warn "Document root not found: $DOMAIN_DOC_ROOT — skipping symlinks."
        return
    fi

    # Symlink media
    MEDIA_LINK="$DOMAIN_DOC_ROOT/media"
    MEDIA_TARGET="$APP_DIR/media"
    if [ -L "$MEDIA_LINK" ]; then
        rm "$MEDIA_LINK"
    fi
    if [ ! -e "$MEDIA_LINK" ]; then
        mkdir -p "$MEDIA_TARGET"
        ln -s "$MEDIA_TARGET" "$MEDIA_LINK"
        log_success "  Media symlink: $MEDIA_LINK → $MEDIA_TARGET"
    fi

    # Symlink static
    STATIC_LINK="$DOMAIN_DOC_ROOT/static"
    STATIC_TARGET="$APP_DIR/staticfiles"
    if [ -L "$STATIC_LINK" ]; then
        rm "$STATIC_LINK"
    fi
    if [ ! -e "$STATIC_LINK" ]; then
        ln -s "$STATIC_TARGET" "$STATIC_LINK"
        log_success "  Static symlink: $STATIC_LINK → $STATIC_TARGET"
    fi
}

#===============================================================================
# Restart Application
#===============================================================================

restart_application() {
    log_info "Restarting application..."

    find "$APP_DIR" -type f -exec chmod 644 {} \; 2>/dev/null || true
    find "$APP_DIR" -type d -exec chmod 755 {} \; 2>/dev/null || true
    chmod 711 "$APP_DIR"
    chmod 644 "$APP_DIR/passenger_wsgi.py" 2>/dev/null || true

    RESTART_FILE="$APP_DIR/tmp/restart.txt"
    mkdir -p "$APP_DIR/tmp"
    touch "$RESTART_FILE"

    log_success "Application restart triggered (Phusion Passenger)."
}

#===============================================================================
# Print Summary
#===============================================================================

print_summary() {
    echo ""
    echo "============================================================"
    echo -e "${GREEN}     FIRST-TIME SETUP COMPLETED SUCCESSFULLY${NC}"
    echo "============================================================"
    echo -e "  Environment:  ${YELLOW}$ENV_NAME${NC}"
    echo -e "  Branch:       ${YELLOW}$BRANCH${NC}"
    echo -e "  Commit:       ${YELLOW}${LATEST_COMMIT:-N/A}${NC}"
    echo -e "  App Dir:      ${YELLOW}$APP_DIR${NC}"
    echo -e "  Python:       ${YELLOW}$(source "$ACTIVATE_ENV" && python --version 2>&1)${NC}"
    echo -e "  Timestamp:    ${YELLOW}$(date '+%Y-%m-%d %H:%M:%S')${NC}"
    echo "============================================================"
    echo -e "  ${BLUE}Next steps:${NC}"
    echo -e "    1. Log in to Wagtail admin and upload content"
    echo -e "    2. For future deploys, use: ${YELLOW}./deployment.sh${NC}"
    echo "============================================================"
    echo ""
}

#===============================================================================
# Main Execution
#===============================================================================

main() {
    echo ""
    echo "============================================================"
    echo -e "${BLUE}   VTP — First-Time Setup Script${NC}"
    echo "============================================================"
    echo -e "  Environment: ${YELLOW}$ENV_NAME${NC}"
    echo -e "  Branch:      ${YELLOW}$BRANCH${NC}"
    echo -e "  Config:      ${YELLOW}$CONFIG_PATH${NC}"
    echo -e "  Env File:    ${YELLOW}$ENV_FILE_PATH${NC}"
    echo "============================================================"
    echo ""

    load_config
    preflight_checks
    pull_latest_code
    sync_code
    copy_env_files
    install_dependencies
    run_migrations
    create_superuser
    setup_pages
    collect_static
    create_symlinks
    restart_application
    print_summary
}

# Run main function
main
