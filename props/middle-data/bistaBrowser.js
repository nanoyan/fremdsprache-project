//#THu: Variablen bzgl. Größe Rechtecke und Linienlänge hinzugefügt. 
let promptElement, pathElement, descriptionElement, detailsElement, svg, root, dataHostElement,
	tree, i = 0,
	duration = 800,
	diagonal, RecHeight = 55,
	RecWidth = 250,
	RecLdHeight = 20,
	RecLdWidth = 10,
	RecRx = 10,
	RecRy = 10,
	LineLength = 320,
	leaves, leaf_bool = false,
	ancestors = [],
	displayMode = 'd3';

document.addEventListener("DOMContentLoaded", () => {
	pathElement = document.getElementsByClassName("path")[0];
	descriptionElement = document.getElementsByClassName("description")[0];
    dataHostElement = document.getElementById("data-host");
	console.log('###');
});

function setMode(mode) {
	if (displayMode !== mode) {
		displayMode = mode;
		if (root) {
			while (dataHostElement.firstChild) {
				dataHostElement.removeChild(dataHostElement.lastChild);
			}
			if (displayMode === 'd3') {
				showDataD3();
			} else {
				showDataText();
			}
		}
	}
}

function showData(dataKey) {
	while (dataHostElement.firstChild) {
		dataHostElement.removeChild(dataHostElement.lastChild);
	}
	
    switch (dataKey) {
        case "IQBItemDBPProps":
            root = IQBItemDBPProps;
            break;
    }
	if (root.name) {
        resetData(root, 0)
    } else {
        transformTreeData(root, 0, "null");
    }
	if (displayMode === 'd3') {
		showDataD3();
	} else {
		showDataText();
	}
}

function showDataText() {
	descriptionElement.innerHTML = "";
	dataHostElement.appendChild(getList(root, 0));
}

function getList(startElement, level) {
	const newListLabel = document.createElement("li");
	newListLabel.innerHTML = (startElement.notation ? startElement.notation + ' ' : '') + startElement.title + (startElement.description ? '<br/>' : '');
	if (startElement.description) {
		const descriptionSpan = document.createElement("p");
		descriptionSpan.classList.add("description-text");
		descriptionSpan.innerHTML = startElement.description;
		newListLabel.appendChild(descriptionSpan);
	}
	newListLabel.classList.add("bista-entry-" + level);

	const children = startElement.children || startElement._children;
	if (children) {
		const newList = document.createElement("ul");
		children.forEach(function (c) {
			newList.appendChild(getList(c, level + 1))
		});
		newListLabel.appendChild(newList)
	};	
	return newListLabel;
}

function showDataD3() {
    pathElement.innerHTML = "Klicken Sie auf einen Knoten, um untere Strukturen einzublenden. Klicken Sie auf Text, um Erläuterungen anzuzeigen.";

    //#THu: Bereich für SVG etwas größer gemacht um Rechtecke so breit wie möglich zu machen
    var margin = {
            top: 5,
            right: 10,
            bottom: 5,
            left: 10
        },
        width = 2450 - margin.right - margin.left,
        height = 1000 - margin.top - margin.bottom;

    tree = d3.layout.tree()
        .size([(height - (RecHeight + margin.top / 2)), width]);

    //#THu: Verbindungslinien auf Mitte der Rechtecke ausrichten
    diagonal = d3.svg.diagonal()
        .source(function (d) {
            return {
                x: d.source.x + RecHeight / 2,
                y: d.source.y + RecWidth
            };
        })
        .target(function (d) {
            return {
                x: d.target.x + RecHeight / 2,
                y: d.target.y
            };
        })
        .projection(function (d) {
            return [d.y, d.x];
        });

    svg = d3.select("#data-host").append("svg")
        // .attr("width", width + margin.right + margin.left)
        // .attr("height", height + margin.top + margin.bottom)
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("preserveAspectRatio", "xMidYMid meet ")
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    //#THu: Workaround: Initialen Baumaufbau hinter Promtleiste ablaufen lassen.
    // Der Baum rutsch dann bereits erstellt von oben ins Fenster, sieht besser aus.
    root.x0 = -100;
    root.y0 = 0;
    if (root.children) {
        root.children.forEach(function (c) {
            if (c.children) {
                c._children = c.children;
                c.children = null;
            }
        });
    }
    dataHostElement.scrollTo(0,0);
    update(root);
    d3.select(self.frameElement).style("height", "500px");
    showDescription(root);
}

function resetData(treeData, level) {
    if (level > 1) {
        if (treeData.children) {
            treeData._children = treeData.children;
            treeData.children = null;
        };
        if (treeData._children) {
            treeData._children.forEach(function (c) {
                resetData(c, level + 1);
            });
        }
    } else {
        if (treeData.children) {
            treeData.children.forEach(function (c) {
                resetData(c, level + 1);
            });
        }
    }
}

function transformTreeData(treeData, level, parentNodeName) {
    treeData.parent = parentNodeName;
    if (level === 0) {
        treeData.name = "root";
        if (treeData.dimensions) {
            treeData.children = treeData.dimensions;
        }
        treeData.children.forEach(function (c) {
            transformTreeData(c, level + 1, "root");
        })
    } else {
		if (treeData.notation) {
			treeData.id = parentNodeName + treeData.notation;
		} else {
			treeData.notation = "";
		}
        treeData.name = (level === 1 ? "" : (parentNodeName + "-")) + treeData.id;
        if (treeData.children) {
            treeData.children.forEach(function (c) {
                transformTreeData(c, level + 1, treeData.name);
            });
            if (level === 1) {
                treeData._children = treeData.children;
                treeData.children = null;
            } else {
                treeData._children = treeData.children;
                treeData.children = null;
            }
        };
    }
}

//Huaning: Added a wrap function for long text
function wrap(text, width) {
    text.each(function () {
        var text = d3.select(this),
            words = text.text().split(/\s+/).reverse(),
            word,
            line = [],
            lineHeight = 1.35, // ems
            y = text.attr("y"),
            dy = parseFloat(text.attr("dy")),
            tspan = text.text(null).append("tspan").attr("x", RecWidth / 2).attr("y", RecHeight * 0.35).attr("dy", dy + "em");
            var counter = 0;
        while (word = words.pop()) {
            line.push(word);
            tspan.text(line.join(" "));
            if (tspan.node().getComputedTextLength() > width) {
                counter += 1;
                line.pop();
                tspan.text(line.join(" "));
                line = [word];
                if(counter === 1){
                    tspan = text.append("tspan").attr("x", RecWidth / 2).attr("y", RecHeight * 0.35).attr("dy", lineHeight + "em").text(word);
                }
                if(counter === 2){
                    tspan = text.append("tspan").attr("x", RecWidth / 2).attr("y", RecHeight * 0.35).attr("dy", (lineHeight+1) + "em").text(word);
                }
                
            }
        }
    });
}

function update(source) {

    //console.log(source.parent)
    // Compute the new tree layout.
    var nodes = tree.nodes(root).reverse();
    var nodes_tmp = nodes.filter(node => node.children || node._children)

    links = tree.links(nodes);
    links_filtered = tree.links(nodes_tmp);
    var nodes_links = links_filtered.filter(function (l){
        return l.target.children == null && l.target._children == null;
    })
    
    var tmp = links_filtered.filter( ( el ) => !nodes_links.includes( el ) );
    // Normalize for fixed-depth.
    nodes.forEach(function (d) {
        d.y = d.depth * (d.children || d._children ? LineLength : LineLength);
    });

    // Update the nodes…
    var node = svg.selectAll("g.node")
        .data(nodes, function (d) {
            return d.id || (d.id = ++i);
        });

    // Enter any new nodes at the parent's previous position.
    var nodeEnter = node.enter().append("g")
        .attr("class", "node")
        .attr("transform", function (d) {
            return "translate(" + (source.y0) + "," + (source.x0) + ")";
        })
        .attr("class", function(d){
            if(d.children || d._children){
                return "inner node"
            } else{
                return "leaf node"
            }
        });

    //#THu:Erzeuge Rechteck statt Kreis und Größe beim Laden
    nodeEnter.append("rect")
        .attr("height", 1e-6)
        .attr("width", 1e-6)
        .on("click", click)


    //#THu: Stelle Text mittig ins Rechteck
    nodeEnter.append("text")
        .attr("dy", ".35em")
        .attr("title", function (d) {
            return d.title
        })
        .attr("text-anchor", function (d) {
            return d.children || d._children ? "middle" : "middle";
        })
        .text(function (d) {
            if (d.depth < 2) {
                return d.title
            } else {
                return d.notation + " " + d.title
            }
        })
        .attr("x", RecWidth / 2)
        .attr("y", RecHeight / 2)
        .style("fill-opacity", 1e-6)
        .call(wrap, RecWidth)
        .on("click", click)

    // Transition nodes to their new position.s
    var nodeUpdate = node.transition()
        .duration(duration)
        .attr("transform", function (d) {
            return "translate(" + d.y + "," + d.x + ")";
        });

    //#THu: Erzeuge Rechteck statt Kreis und animiere auf finale Größe
    nodeUpdate.select("rect")
        .duration(1)
        .attr("width", RecWidth)
        .attr("height", RecHeight)
        .attr("rx", RecRx)
        .attr("ry", RecRy);
    d3.selectAll("rect").style("fill", function (d) {
        return d.children ? "#fff" : (d._children || d.__children ? "rgb(213,213,213)" : "#fff");
    });
    d3.selectAll(".leaf.node").selectAll("rect").style("fill", "#d1e0e0")

    nodeUpdate.select("text")
        .style("fill-opacity", 1);
    // Transition exiting nodes to the parent's new position.
    var nodeExit = node.exit().transition()
        .duration(duration)
        .attr("transform", function (d) {
            return "translate(" + source.y + "," + source.x + ")";
        })
        .remove();

    leaves = d3.selectAll("rect").filter(function (d) {
        return d.children == null && d._children == null
    })
    //#THu
    nodeExit.select("rect")
        .attr("width", RecWidth)
        .attr("height", RecHeight)
        .style("fill-opacity", 1e-6);
    nodeExit.select("text")
        .style("fill-opacity", 1e-6);
    // Update the links…
    var link = svg.selectAll("path.link")
        .data(links, function (d) {
            return d.target.id;
        });


    // Enter any new links at the parent's previous position.
    link.enter().insert("path", "g")
        .attr("class", "link")
        .attr("d", function (d) {
            var o = {
                x: source.x0,
                y: source.y0
            };
            return diagonal({
                source: o,
                target: o
            });
        });

    // Transition links to their new position.
    link.transition()
        .duration(duration)
        .attr("d", diagonal);

    // Transition exiting nodes to the parent's new position.
    link.exit().transition()
        .duration(duration)
        .attr("d", function (d) {
            var o = {
                x: source.x,
                y: source.y
            };
            return diagonal({
                source: o,
                target: o
            });
        })
        .remove();

    // Highlight the path from root to clicked node
    link.filter(function (d) {
            if (ancestors.indexOf(d.target) !== -1) {
                // Resets all link colors and stroke-width to default values
                d3.selectAll("path").style("stroke", "#353563").style("stroke-width", "1");
                return true;
            }
        }).style("stroke", "#74cde8")
        .style("stroke-width", "3");

    // Stash the old positions for transition.
    nodes.forEach(function (d) {
        d.x0 = d.x;
        d.y0 = d.y;
    });
}

function updateAncestors(d) {
    ancestors = [];
    if(d.children || d._children){
        ancestors.push(d);
    }
    

    while (d.parent) {
        d = d.parent;
        ancestors.push(d);
    }
}

// Toggle children on click.
function click(d) {
    if (d.name === "root") {
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else {
            d.children = d._children;
            d._children = null;
        }
        resetData(d, 0);
    } else {
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else {
            d.children = d._children;
            d._children = null;
        }
        // HY: This part is used to display more layers of the graph as nodes
        if (d.__children) {
            d._children = d.__children;
            d.__children = null;
        }


        const p = d.parent;
        p.children.forEach(function (c) {
            if (c.children && c.name !== d.name) {
                c._children = c.children;
                c.children = null;
            }
        });
    }
    updateAncestors(d);
    update(d);
    showDescription(d);
}

function showDescription(node) {
    descriptionElement.innerHTML = node.description || node.title;
    let path = "";
    do {
        path = " &rtri; " + node.title + path;
        node = node.parent;
    } while (node.parent !== undefined);
    pathElement.innerHTML = path;
}