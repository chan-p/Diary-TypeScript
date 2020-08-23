apt-get install nginx
nginx

apt-get install language-pack-ja-base language-pack-ja
locale-gen ja_JP.UTF-8
echo export LANG=ja_JP.UTF-8 >> ~/.profile
source ~/.profile
