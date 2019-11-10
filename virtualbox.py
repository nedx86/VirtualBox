#! /usr/bin/python3
# -*- coding: utf-8 -*-

import getpass
import pexpect
import time
import argparse
import sys
import os

def action(vm_name, vm_action):
    cmd = ""

    if vm_action == "start":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage startvm '{}' --type headless\"".format(vm_name),"r")

    if vm_action == "show":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage startvm '{}' --type separate\"".format(vm_name),"r")

    if vm_action == "stop":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage controlvm '{}' acpipowerbutton\"".format(vm_name),"r")

    if vm_action == "shutdown":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage controlvm '{}' poweroff\"".format(vm_name),"r")

    if vm_action == "reboot":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage controlvm '{}' reset\"".format(vm_name),"r")

    if vm_action == "save":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage controlvm '{}' savestate\"".format(vm_name),"r")

    if vm_action == "pause":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage controlvm '{}' pause\"".format(vm_name),"r")

    if vm_action == "resume":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage controlvm '{}' resume\"".format(vm_name),"r")

    if vm_action == "state":
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage list vms --long | grep -e 'Name:' -e 'State:'\"","r")

    if (vm_action == "saveall"):
        vms = []
        cmd = os.popen("sudo -H -u $USER bash -c \"VBoxManage list runningvms | sed -r 's/.*\{(.*)\}/\\1/'\"","r")
        while 1:
            line = cmd.readline()
            if not line: break
            vms.append(line.replace('\n', ''))
            print (vms)
        for vm in vms:
            action(vm, "save")
            print(vm)
        while 1:
            line = cmd.readline()
            if not line: break
            print (line.encode("UTF-8"))
        print("\n")

cmd = ""
parser = argparse.ArgumentParser(description='VirtualBox Client')
parser.add_argument('--name', help='Name')
parser.add_argument('--action', help='Action')
args = parser.parse_args()
vm_name = args.name
vm_action = args.action

action(vm_name, vm_action)
