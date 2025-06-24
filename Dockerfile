FROM public.ecr.aws/lambda/python:3.13

RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm \
    libgbm libxkbcommon libdrm

COPY handler.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

ENV SE_CACHE_PATH=/tmp

RUN dnf install -y shadow-utils && \
    /usr/sbin/useradd --uid 1000 user
USER user

CMD ["handler.lambda_handler"]
