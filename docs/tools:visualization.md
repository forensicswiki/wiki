---
tags:
  -  Tools
  -  Log Analysis
---
Although not strictly for forensic purposes, **visualization tools**
such as the ones discussed here can be very useful for visualizing large
data sets. As forensic practitioners need to process more and more data,
it is likely that some of the techniques implemented by these tools will
need to be adopted.

## Programming Languages and Developer Toolkits

If you are building forensic tools, you probably want to start with one
of these:

### Java

Advantage: Portable and lots of good documentation out there.

Disadvantage: Programs are a bit verbose, and only offers about 1/2 the
performance of C

- [Graph Interface Library
  (GINY)](http://csbi.sourceforge.net/index.html) - Java
- [HyperGraph](http://hypergraph.sourceforge.net/) - Hyperbolic trees,
  in Java. Check out the home page. Try clicking on the logo...
- [InfoViz Toolkit](http://ivtk.sourceforge.net/) - Java, originally
  developed at [INRA](inra.md).
- [Jdigrah](https://jdigraph.dev.java.net/) - Java Directed Graphs.
- [JGraphT](http://jgrapht.sourceforge.net/) - A Java visualization kit
  designed to be simple and extensible.
- [Perfuse](http://prefuse.sourceforge.net/) - A Java-based toolkit for
  building interactive information visualization applications
- [VisAD](http://www.ssec.wisc.edu/~billh/visad.html#intro) - A Java
  component library for interactive and collaborative visualization.
- [Linguine
  Maps](http://www.softwaresecretweapons.com/jspwiki/Wiki.jsp?page=LinguineMaps) -
  An open-source Java-based system for visualizing software call maps.
- [Zoomable Visual Transformation
  Machine](http://zvtm.sourceforge.net/index.html) - Java. Originally
  started at Xerox Research Europe.
- [OpenMap](http://openmap.bbn.com/) A Java-based Geographical
  Information System framework, from [BBN](bbn.md).

### Python

Advantage: Portable

Disadvantage: Python is one of the slowest modern languages around and
doesn't work well with big data sets.

- Python with Tk
- Python with matplotlib
- Python with wxWidgets (not installed by default)
- [NetworkX](http://networkx.lanl.gov/), a pure Python network layout
  program which uses matplotlib to do the actual graphing.

### Processing.org

Advantage: Programming language specifically developed for
visualization; compiles to java byte code

Disadvantage: Very oddball

- [processing.org](http://processing.org) and

### JavaScript

Browsers are now very fast and there are a large number of data plotting
systems built on JavaScript. Check out:

- [processingjs.org](http://processingjs.org)
- [Highcharts JS](http://highcharts.com/)
- [D3 - Data Driven Documents](http://mbostock.github.com/d3/) - A
  visualization library for the Web.
- [KeyLines](http://key-lines.com) - Commercially licensed visualization
  library for networks/graphs.

### C/C++

- [The Visualization Toolkit](http://www.vtk.org/) - C++ multi-platform
  with interfaces available for Tcl/Tk, Java and Python.

## Applications

Most of these applications can be used to do visualization

Crystal Space 3D

<!-- -->

Panda#D

### Data Plotting Applications

- <http://ploticus.sourceforge.net>
- <http://www.gnuplot.info/>
- <http://tulip.labri.fr/TulipDrupal/>

### Graph and (Social) Network Visualization

- [Cytoscape](http://www.cytoscape.org/) - Cytoscape is an open source
  software platform for visualizing complex networks and integrating
  these with any type of attribute data.
- [Graphviz](http://www.graphviz.org/) - Originally developed by the
  [AT&T Information Visualization
  Gorup](http://public.research.att.com/areas/visualization/), designed
  for drawing connected graphs of nodes and edges. Neato is a similar
  system but does layout based on a spring model. Can produce output as
  [PostScript](postscript.md), [PNG](png.md),
  [GIF](gif.md), or as an annotated graph file with the
  locations of all of the objects — ideal for drawing in a GUI. Runs
  from the command line on [Unix](unix.md),
  [Windows](windows.md) and [Mac](mac_os_x.md), although
  there is also a [MacOS GUI
  version](http://www.pixelglow.com/graphviz/).
- [NodeXL](http://www.codeplex.com/nodexl) - Free/open excel add-in
  extends the spreadsheet with network metrics and visualizations. (Only
  runs on Windows)
- [Gephi](http://gephi.org/) -Gephi is an interactive visualization and
  exploration platform for all kinds of networks and complex systems,
  dynamic and hierarchical graphs

<!-- -->

- <http://projects.skewed.de/graph-tool/> - graph-tool is an efficient
  python module for manipulation and statistical analysis of graphs
  (a.k.a. networks).
- <http://igraph.sourceforge.net/> - Integrates with R.
- <http://socnetv.sourceforge.net/> - "Social Networks Visualizer
  (SocNetV) is a flexible and user-friendly tool for the analysis and
  visualization of Social Networks."
- [NetDraw](https://sites.google.com/site/netdrawsoftware/home) - "a
  free program written by Steve Borgatti for visualizing both 1-mode and
  2-mode social network data."
- [Pajek](http://pajek.imfm.si/doku.php) - Windows program for drawing
  large networks.
- [Social Network Image Animator
  (SoNIA)](https://sourceforge.net/projects/sonia/) - Originally
  developed at Stanford. Written in Java. Makes movies.
- [Walrus](http://www.caida.org/tools/visualization/walrus/) - A 3-d
  graph network exploration tool. Employs 3D hyperbolic displays and
  layout based on a user-supplied spanning tree.
- [AfterGlow](http://afterglow.sf.net) - A tool to simplify the
  generation of network graphs in GraphViz, Gephi, etc. Designed for
  security visualizations.
- <http://tulip.labri.fr/TulipDrupal/> - Tulip is an information
  visualization framework dedicated to the analysis and visualization of
  relational data.

See also:
<http://en.wikipedia.org/wiki/Social_network_analysis_software>

Reas govisual diagram editor reas.com gdf.net

### Commercial Graphic Applications and Tools

- [aiSee Graph Layout Software](http://www.aisee.com/) - Supports 15
  layout algorithms, recursive graph nesting, and easy printing. Runs on
  [Windows](windows.md), [Linux](linux.md),
  [Solaris](solaris.md), [NetBSD](netbsd.md), and
  [MacOS](mac_os_x.md). 30-day trial and free registered versions
  available. Academic pricing available.
- [Geomantics](http://www.geomantics.com/) - Geographical, Visualization
  and Graphics software. Runs on [Windows](windows.md).
- [Graphis 2D and 3D graphing software](http://www.kylebank.com/) - Runs
  on [Windows](windows.md). Free 30-day evaluation copy
  available.
- [OpenViz](http://www.openviz.com/) and
  [PowerViz](http://www.powerviz.com/) - Both from Advanced Visual
  Systems, super high-end visualization toolkits. \$\$\$\$
- [Tom Sawyer Software](http://www.tomsawyer.com/) Analysis,
  Visualizaiton, and Layout programs. - Heavy support for drawing
  graphs. Beautiful gallery. ActiveX, Java, C++ and .NET editions.
- [NetMiner](http://www.netminer.com/) - A comprehensive tool for Social
  Network Analysis. Runs on Windows, with a Linux version under
  development. \$35 for "Express" student version, \$250 for
  "Professional" student version, \$950 for "Normal" "Professional"
  version.
- [UCINET](http://www.analytictech.com/ucinet.htm) - A comprehensive
  package for the analysis of social network data as well as other
  1-mode and 2-mode data.
- [Logster](http://www.clarifiednetworks.com/logster) - an ultra-easy
  software tool to visualize Apache-style logs on a world map.
- [Clarified
  Analyzer](http://www.clarifiednetworks.com/Clarified%20Analyzer) -
  Visualizes Network Traffic and allows to drill down from
  visualizations to the packet level.

### Unclassified

- [Gravisto: Graph Visualization
  Toolkit](http://gravisto.fim.uni-passau.de/) - An editor and toolkit
  for developing graph visualization algorithms.
- [Rox Graph Theory Framework](http://www.gnu.frb.br:8080/rox) - An
  open-source plug-in framework for graph theory visualization.
- [TouchGraph](http://touchgraph.sourceforge.net/) - Library for
  building graph-based interfaces.

## See Also

- [Network Data Visualizations](network_data_visualizations.md)
- [GVU's Information Visualization Resources link
  farm](http://www-static.cc.gatech.edu/gvu/ii/resources/infovis.html)
- [Google Directory of Graph Drawing
  Software](http://directory.google.com/Top/Science/Math/Combinatorics/Software/Graph_Drawing/)
- [GNU Free Software directory of scientific visualization
  software](http://directory.fsf.org/science/visual/)
- [Open Source Graph Network Visualization in
  Java](http://www.manageability.org/blog/stuff/open-source-graph-network-visualization-in-java/view)
- [INSNA's web page of Computer Programs for Social Network
  Analysis](http://www.insna.org/INSNA/soft_inf.html)
- <http://www.ontopia.net/omnigator/models/index.jsp>
- <http://visant.bu.edu/>
- <https://sourceforge.net/projects/touchgraph/>
- [Christian Tominski](http://www.informatik.uni-rostock.de/~ct/)

CAIDA has 15+ years of work visualizing Internet topologies. You may
find their tools to be useful:

- <http://www.caida.org/tools/visualization/>
- <http://www.caida.org/publications/visualizations/>
- <http://www.caida.org/tools/visualization/walrus/gallery1/>
- <http://www.caida.org/research/topology/as_core_network/>
