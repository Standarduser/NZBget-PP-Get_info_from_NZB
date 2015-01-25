#!/usr/bin/env python
#coding: utf8 

import os
import sys

##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###
#
# Dieses Script schreibt alle verfügbaren Informationen ins Log.
# 
### NZBGET POST-PROCESSING SCRIPT                                          ###
##############################################################################

POSTPROCESS_SUCCESS=93
POSTPROCESS_ERROR=94

##############################################################################
# 
# NZBPP_DIRECTORY	path to destination dir for downloaded files.
# 
# NZBPP_NZBNAME		User-friendly name of processed nzb-file as it is displayed by the 
# 					program. The file path and extension are removed. If download was 
# 					renamed, this parameter reflects the new name.
# 
# NZBPP_NZBFILENAME	Name of processed nzb-file. If the file was added from incoming 
# 					nzb-directory, this is a full file name, including path and extension.
# 					If the file was added from web-interface, it's only the file name with
# 					extension. If the file was added via RPC-API (method append), this can
# 					be any string but the use of actual file name is recommended for
# 					developers.
# 
# NZBPP_CATEGORY	Category assigned to nzb-file (can be empty string).
# 
# NZBPP_TOTALSTATUS	Total status of nzb-file:
# 					SUCCESS - everything OK;
# 					WARNING - download is damaged but probably can be repaired; user 
# 								intervention is required;
# 					FAILURE - download has failed or a serious error occurred during 
# 								post-processing (unpack, par);
# 					DELETED - download was deleted; post-processing scripts are usually 
# 								not called in this case; however it's possible to force 
# 								calling scripts with command "post-process again".
# 
# NZBPP_STATUS		Complete status info for nzb-file: it consists of total status and 
# 					status detail separated with slash. There are many combinations. Just 
# 					few examples:
# 					
# 					FAILURE/HEALTH;
# 					FAILURE/PAR;
# 					FAILURE/UNPACK;
# 					WARNING/REPAIRABLE;
# 					WARNING/SPACE;
# 					WARNING/PASSWORD;
# 					SUCCESS/ALL;
# 					SUCCESS/UNPACK.
# 					
# 					For the complete list see description of method history in RPC API 
# 					reference.
# 
# 					NOTE: one difference to the status returned by method history is that 
# 					NZBPP_STATUS assumes all scripts are ended successfully. Even if one 
# 					of the scripts executed before the current one has failed the status 
# 					will not be set to WARNING/SCRIPT as method history will do. For 
# 					example for a successful download the status would be SUCCESS/ALL 
# 					instead. Because most scripts don't depend on other scripts they 
# 					shouldn't assume the download has failed if any of the previous 
# 					scripts (such as a notification script) has failed. The scripts 
# 					interested in that info still can use parameter NZBPP_SCRIPTSTATUS.
# 
# 					NOTE: new in v13.
# 
# NZBPP_SCRIPTSTATUS	Summary status of the scripts executed before the current one:
# 					
# 					NONE - no other scripts were executed yet or all of them have ended 
# 							with exit code "NONE";
# 					SUCCESS - all other scripts have ended with exit code "SUCCESS" ;
# 					FAILURE - at least one of the script has failed.
# 					
# 					NOTE: new in v13.

##############################################################################

print 100*'-'
print 'NZBPP_DIRECTORY: ' + os.environ['NZBPP_DIRECTORY']
print 'NZBPP_NZBNAME: ' + os.environ['NZBPP_NZBNAME']
print 'NZBPP_NZBFILENAME: ' + os.environ['NZBPP_NZBFILENAME']
print 'NZBPP_CATEGORY: ' + os.environ['NZBPP_CATEGORY']
print 'NZBPP_TOTALSTATUS: ' + os.environ['NZBPP_TOTALSTATUS']
print 'NZBPP_STATUS: ' + os.environ['NZBPP_STATUS']
print 'NZBPP_SCRIPTSTATUS: ' + os.environ['NZBPP_SCRIPTSTATUS']
print 100*'-'

sys.exit(POSTPROCESS_SUCCESS)