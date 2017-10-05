
Following was the data from Route Views project:
Host                                 File                       # IPv4 entries
route-views2.oregon-ix.net           rib.20160320.2200.bz2       
route-views.sydney.routeviews.org    rib.20160320.2000.bz2    
route-views.saopaulo.routeviews.org  rib.20160329.1600.bz2   
route-views.wide.routeviews.org      rib.20160630.2000.bz2 
route-views.linx.routeviews.org      rib.20160628.0200.bz2


rib.20160320.2200.bz2 route-views2.oregon-ix.net
rib.20151001.0000.bz2.route-views3
rib.20160101.0000.bz2.bgpdata
oix-full-snapshot-2016-01-19-1400.bz2
rib.20160123.1600.bz2.route-views.eqix

1. download and uncompress file 
download compressed rib file from route view project, the file suffix is .bz2
download and compiler libbgpdump tools.

bunzip2 rib.20160101.0000.bz2

bgpdump -M rib.20160101.0000 > rib.20160101.0000.M.txt

2. extract the rib file
./RouteViewData.py -r rib.20160123.1600.M.txt 

