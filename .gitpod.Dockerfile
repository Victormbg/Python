FROM gitpod/workspace-full-vnc

USER gitpod

# Instale pacotes necessários para Python
RUN sudo apt-get update && \
    sudo apt-get install -y python3-pyqt5 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install matplotlib jupyter