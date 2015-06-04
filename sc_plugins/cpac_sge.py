from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class PEInstaller(ClusterSetup):
	def __init__(self, pe_url):
		self.pe_url = pe_url
		log.debug('pe_url = %s' % pe_url)
	def run(self, nodes, master, user, user_shell, volumes):
		log.info('Installing C-PAC\'s Parallel Environment')
		mssh = master.ssh
		mssh.execute('cd /tmp && wget %s' % self.pe_url)
		mssh.execute('qconf -Ap /tmp/mpi_smp.conf')
		mssh.execute('qconf -mattr queue pe_list "mpi_smp" all.q')
