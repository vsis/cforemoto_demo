FROM base/archlinux
MAINTAINER Roddy González <roddy.gonzalez.89@gmail.com>

ADD src/ /
ADD requirements.txt /

RUN pacman -Sy  --noconfirm  archlinux-keyring ; \
    pacman -S   --noconfirm --needed firefox geckodriver sqlite python python-pip python-setuptools tigervnc ; \
    pacman -Scc --noconfirm ; \
    pip install -r /requirements.txt

EXPOSE 8080

CMD ["python", "uf_api/manage.py", "runserver", "0.0.0.0:8080"]
