# Dockerfile by hdf: build a docker image
# usage: docker build -t user/centos .
# usage: docker run -dt --privileged user/centos
# usage: docker exec -it containerid /bin/bash

FROM centos:7
MAINTAINER hdf <qihdf@qq.com>

# change system environments
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# change system local time
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# fix: warning: rpmts_HdrFromFdno
RUN rpm --import /etc/pki/rpm-gpg/RPM*

# update yum and install something
RUN yum update -y
RUN yum install -y xz
RUN yum install -y vim
RUN yum install -y git
RUN yum install -y gcc
RUN yum install -y make
RUN yum install -y wget
RUN yum install -y screen
RUN yum install -y gcc-c++
RUN yum install -y crontabs
RUN yum install -y zlib-devel
RUN yum install -y sqlite-devel
RUN yum install -y openssl-devel

# install python
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u
RUN yum install -y python36u-pip
RUN yum install -y python36u-devel

# install nginx
RUN yum install -y epel-release
RUN yum install -y nginx

# clean yum cache
RUN yum clean all

# install libs of python3
ADD ./requirements.txt /root/
WORKDIR /root/
RUN pip3.6 install --upgrade pip
RUN pip3.6 install -r requirements.txt

# clean everything
RUN rm -rf /root/*

# cmd command
# CMD /bin/bash
ENTRYPOINT /usr/sbin/init
