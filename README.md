# graph_profile

IPython magic to create call graph with timings


# usage

to install:

```
pip install git+https://github.com/pashenkogleb/graph_profile
sudo apt install graphviz
pip install gprof2dot
```

to use:
```
import graph_profile

%%graph_profile [optional_filename for jpg image]
CODE
```


# how it works

cprofile to create profiler objects

gprof2dot to create dot graph

```
%%prun -q -D out.profile
SOME_CODE
```
```
! gprof2dot -f pstats out.profile  > temp.dot
! dot -Tjpg temp.dot -o outfile.jpg
```
