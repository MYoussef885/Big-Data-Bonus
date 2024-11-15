#!/bin/bash
# Copy output files from the container to the local directory
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt service-result/
docker stop bd-a1-container