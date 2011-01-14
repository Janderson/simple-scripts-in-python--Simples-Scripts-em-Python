from subprocess import Popen, PIPE
import os
p = Popen("svn stat", shell=True, stdin=PIPE, stdout=PIPE)
stdout_str, strerr_str = p.communicate()
arq_adicionar = []
arq_commitar = []

remover = ["tmp/cache", "commit.all.svn.py", "log/development.log", "db/development.sqlite3", "tmp/pids/server.pid"]
for lin in stdout_str.split("\n"):
  it = lin.replace("\n", "").split("       ")
  if it[0] == "?":
    arq_adicionar.append(it[1])
    arq_commitar.append(it[1])
  elif it[0] == "A":
    arq_commitar.append(it[1])
  elif it[0] == "M":
    arq_commitar.append(it[1])
    
for par in arq_adicionar:
  os.system("svn add " + str(par))
for i in remover:
  try:
    arq_commitar.remove(i)
  except:
    pass
p = Popen("svn ci " + " ".join(arq_commitar) + " -m 'comitado'", shell=True, stdin=PIPE, stdout=PIPE)
stdout_str, strerr_str = p.communicate()
print stdout_str, strerr_str
