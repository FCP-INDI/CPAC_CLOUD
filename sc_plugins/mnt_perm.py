from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class MntPermissions(ClusterSetup):
    def __init__(self):
        log.debug('Changing permissions of /mnt to world-readable.')
    def run(self, nodes, master, user, user_shell, volumes):
        for node in nodes:
            log.info("Changing permissions of /mnt on %s" % node.alias)
            node.ssh.execute('chmod -R 777 /mnt')
