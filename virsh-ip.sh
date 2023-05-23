#!/bin/bash
BASE_DIR=$(cd $(dirname $0); pwd)
VIRSH_NAME=$1
IP_HEAD=10.251.1

if [ "$1"x == "all"x ] || [ ! -n "$1" ]
then
    VIRSH_NAME=$(virsh list | egrep -v "^$|名称|-----" | awk '{print $2}')
else
    VIRSH_NAME=$1
fi

# 环境恢复,删除log文件
if [ -f ${BASE_DIR}/virsh-ip.log ]
then
    rm ${BASE_DIR}/virsh-ip.log
fi

function PING_ALL_IPADDR () {
    for i in $(seq 1 255)
        do
            {
                ping ${IP_HEAD}.${i} -c 1 -w 1 > /dev/null  2>&1
            } &
        done
    wait
}

function FIND_VIRSH () {
VIRSH_NAME_ARRAY=($(printf "%q\n" ${VIRSH_NAME}))

for (( n=0 ; n<${#VIRSH_NAME_ARRAY[@]} ; n++ ))
    do
        VIRSH_MAC=$(virsh domiflist ${VIRSH_NAME_ARRAY[n]} | egrep -v "MAC|-----|^$" | awk '{print $NF}')
        echo "${VIRSH_NAME_ARRAY[n]}:" >> ${BASE_DIR}/virsh-ip.log
        arp -n | grep -i ${VIRSH_MAC} | awk '{print "ip:"$1 "\t" "mac:"$3}' >> ${BASE_DIR}/virsh-ip.log
        echo " " >> ${BASE_DIR}/virsh-ip.log
    done

printf "\e[1;35m Get IP complate,Use command: cat ${BASE_DIR}/virsh-ip.log\e[0m\n"
}

function main () {
    printf "\e[1;35m I'm just coming!\e[0m\n"
    PING_ALL_IPADDR
    FIND_VIRSH
}

main
