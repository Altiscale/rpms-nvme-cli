# rpms-nvme-cli

Altiscale build of nvme-cli

Included is the spec file only to build on Cent OS 6 (adapted from the Cent OS 7 src rpm). The source comes from elsewhere on github. 

Cent OS 6 has no useful, native nvme support. Our Linux kernel build works with nvme SSDs just fine, but it is helpful to have the nvme command to manage nvme devices (particularly error and SMART logging).

https://github.com/linux-nvme/nvme-cli

