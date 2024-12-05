FROM python:3.11-slim

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1 \
#  Python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
# pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Prepare system
RUN apt-get update \
    && apt-get install \
      --no-install-recommends --no-install-suggests -y \
      gettext \
      build-essential \
      zlib1g-dev \
      libjpeg-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y \
    && apt-get clean \
    && mkdir /local \
    && addgroup --gid 4000 user-m \
    && adduser --system --disabled-password --disabled-login --gecos "" --gid 4000 --uid 4000 user-m \
    && chown -R user-m:user-m /local \
    && chsh -s /bin/false user-m

# Install python environment and requirements
COPY --chown=user-m:user-m requirements.txt /local/requirements.txt
RUN pip install --upgrade pip
WORKDIR /local
RUN pip install -r requirements.txt

# Add application code
COPY --chown=user-m:user-m . /local
EXPOSE 8000
WORKDIR /local
COPY entrypoint.sh /entrypoint.sh

RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT [ "/bin/sh", "-c", "/entrypoint.sh" ]