FROM gitpod/workspace-postgresql

USER gitpod

# Install some tooling need to develop
# - Task https://taskfile.dev/
# - Mockintosh https://mockintosh.io/
# - pipx https://pypa.github.io/pipx/
# ====== Go
RUN bash -c "brew install go-task/tap/go-task"

# ====== Python
RUN bash -c "python3 -m pip install --user pipx && \
    python3 -m pipx ensurepath --force"