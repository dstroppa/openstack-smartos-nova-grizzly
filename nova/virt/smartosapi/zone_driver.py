# coding=utf-8
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2012 Hendrik Volkmer
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.virt.smartosapi.vm_driver import VmDriver


class ZoneDriver(VmDriver):

    def startinfo(self):
        return {
           "brand": "joyent",
           "hostname": (self.instance['server_name'] or self.instance['uuid']),
           "max_physical_memory": self.instance['memory_mb'],
           "dataset_uuid": self.image_id,
           "internal_metadata": {
             "created_by_openstack": True,
             },
           "vcpus": self.instance['vcpus'],
           "uuid": self.instance['uuid'],
           "owner_uuid": self.instance['project_id'],
           "nics": [
             {
               "nic_tag": "admin",
               "ip": self.nics["ips"][0]["ip"],
               "netmask": self.nics["ips"][0]["netmask"],
               "gateway": self.nics["ips"][0]["gateway"]
               }
             ]
           }
