#!/bin/sh

rvtl64 linenum.vtl runq.vtl - 10000 rvtlwiki.vtx     > rvtlwiki.cgi
rvtl64 linenum.vtl runq.vtl - 10000 render.vtx       > render.cgi
rvtl64 linenum.vtl runq.vtl - 10000 rvtlwiki64.vtx   > rvtlwiki64.cgi
rvtl64 linenum.vtl runq.vtl - 10000 render64.vtx     > render64.cgi

echo You should remove line numbers at first 2 lines and last 2 lines.
