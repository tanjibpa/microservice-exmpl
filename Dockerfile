FROM centos:8
# Install 'build-base' meta-package for gcc and other packages needed
# to compile dependencies listed in requirements.txt

WORKDIR /micro

COPY requirements.txt /micro/requirements.txt
RUN yum install -y python3 python3-devel postgresql-libs postgresql-devel gcc
RUN pip3 install --upgrade pip && pip install cython && pip install --no-cache-dir -r /micro/requirements.txt

ENV FLASK_APP="/micro/app.py"
CMD flask db init && flask db upgrade

COPY . /micro
