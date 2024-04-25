FROM continuumio/miniconda3

WORKDIR /

# Create the environment:
RUN conda update conda -y
COPY environment.yaml .
RUN conda env create -f environment.yaml

# Make RUN commands use the new environment:
RUN echo "conda activate tudat-space" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure Tudat is installed:"
RUN python -c "import numpy"

# The code to run when container is started:
COPY main.py entrypoint.sh ./
COPY SW-All.txt ./
COPY requirements.txt ./
COPY resource /root/.tudat/resource
ENTRYPOINT ["./entrypoint.sh"]