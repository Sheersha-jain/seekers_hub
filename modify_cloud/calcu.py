#! /usr/bin/python
import commands
commands.getoutput("yum install -y sshpass")  ## install sshpass package on client side
commands.getoutput("sshpass -p redhat ssh -Y root@192.168.0.201 gcalctool")
