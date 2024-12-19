# Use Python base image
FROM --platform=linux/amd64 python:3

# Set environment variables
ENV ANSIBLE_HOME=/ansible
WORKDIR $ANSIBLE_HOME

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sshpass \
        libffi-dev \
        libssl-dev \
        build-essential \
        python3-dev \
        python3-pip \
        git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Ansible and required Python packages
RUN pip install ansible requests unificontrol

# Install Ansible collections
RUN ansible-galaxy collection install community.general

# Default shell entry point for manual use (Option 1)
CMD ["/bin/sh"]

# Uncomment the following lines for Option 2: Automatically run a specific playbook
# ENTRYPOINT ["ansible-playbook"]
# CMD ["playbooks/collect_unifi_inventory.yml"]

# Notes:
# - Option 1 (default): The container starts with a shell, allowing you to manually run Ansible commands or playbooks.
# - Option 2: Uncomment the ENTRYPOINT and CMD lines above to automatically run the specified playbook when the container starts.
