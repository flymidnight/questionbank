from modulefinder import packagePathMap


login_url =  "https://www.examtopics.com/login/"
logout_url = "https://www.examtopics.com/logout/"
pocketprep_login_url = "https://study.pocketprep.com/sign-in?type=password"
pro_login_url = "https://unlimited.examtopics.com/login"
login_itexams_url =  "https://www.itexams.com/accounts/login/"
logout_itexams_url = "https://www.itexams.com/accounts/logout/"
user_name = "goldeneye"
password = "Iaalet3*22"
pro_user_name = "jeremy.pu@gmail.com"
pro_password = "Iaalet3*22"
pocketprep_user_name = "flymidnighter@gmail.com"
pocketprep_password = "Iaalprep3*44"
examheist_user_name = "flymidnighter@gmail.com"
itexams_user_name = "flymidnighter"
itexams_password = "Wsnbb399"
exams =     [["pl-600", "pl-600", "https://www.examtopics.com/exams/microsoft/pl-600/view/", 255],
            ["AWS Certified DevOps Engineer - Professional DOP-C02", "dop-c02", "https://www.examtopics.com/exams/amazon/aws-certified-devops-engineer-professional-dop-c02/view/", 418],
            ["AWS Certified Security - Specialty SCS-C03", "scs-c03", "https://www.examtopics.com/exams/amazon/aws-certified-security-specialty-scs-c03/view/", 62],
            ["az-104", "az-104", "https://www.examtopics.com/exams/microsoft/az-104/view/", 606],
            ["az-204", "az-204", "https://www.examtopics.com/exams/microsoft/az-204/view/", 487],
            ["AWS Certified Advanced Networking - Specialty ANS-C01", "ans-c01", "https://www.examtopics.com/exams/amazon/aws-certified-advanced-networking-specialty-ans-c01/view/", 272],
            ["az-400", "az-400", "https://www.examtopics.com/exams/microsoft/az-400/view/", 564],
            ["pl-400", "pl-400", "https://www.examtopics.com/exams/microsoft/pl-400/view/", 429],
            ["pl-900", "pl-900", "https://www.examtopics.com/exams/microsoft/pl-900/view/", 351],
            ["Professional Cloud Architect", "gcp-pca", "https://www.examtopics.com/exams/google/professional-cloud-architect/view/", 346],
            ["Associate Cloud Engineer", "gcp-ace", "https://www.examtopics.com/exams/google/associate-cloud-engineer/view/", 336],
            ["dp-900", "dp-900", "https://www.examtopics.com/exams/microsoft/dp-900/view/", 314],
            ["az-305", "az-305", "https://www.examtopics.com/exams/microsoft/az-305/view/", 286],
            ["pl-200", "pl-200", "https://www.examtopics.com/exams/microsoft/pl-200/view/", 318],
            ["Professional Data Engineer", "gcp-pde", "https://www.examtopics.com/exams/google/professional-data-engineer/view/", 338],
            ["AWS Certified Machine Learning - Specialty", "mls-c01", "https://www.examtopics.com/exams/amazon/aws-certified-machine-learning-specialty/view/", 369],
            ["AWS Certified Cloud Practitioner CLF-C02", "clf-c02", "https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner-clf-c02/view/", 719],
            ["AWS Certified Database - Specialty", "dbs-c01", "https://www.examtopics.com/exams/amazon/aws-certified-database-specialty/view/", 359],
            ["az-500", "az-500", "https://www.examtopics.com/exams/microsoft/az-500/view/", 505],
            ["dp-100", "dp-100", "https://www.examtopics.com/exams/microsoft/dp-100/view/", 527],
            ["dp-300", "dp-300", "https://www.examtopics.com/exams/microsoft/dp-300/view/", 373],
            ["dp-500", "dp-500", "https://www.examtopics.com/exams/microsoft/dp-500/view/", 194],
            ["dp-600", "dp-600", "https://www.examtopics.com/exams/microsoft/dp-600/view/", 198],
            ["dp-700", "dp-700", "https://www.examtopics.com/exams/microsoft/dp-700/view/", 118],
            ["az-700", "az-700", "https://www.examtopics.com/exams/microsoft/az-700/view/", 369],
            ["az-800", "az-800", "https://www.examtopics.com/exams/microsoft/az-800/view/", 292],
            ["ai-102", "ai-102", "https://www.examtopics.com/exams/microsoft/ai-102/view/", 333],
            ["ai-900", "ai-900", "https://www.examtopics.com/exams/microsoft/ai-900/view/", 246],
            ["ms-900", "ms-900", "https://www.examtopics.com/exams/microsoft/ms-900/view/", 507],
            ["AWS Certified Solutions Architect - Associate SAA-C03", "saa-c03", "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate-saa-c03/view/", 1019],
            ["pl-300", "pl-300", "https://www.examtopics.com/exams/microsoft/pl-300/view/", 371],
            ["AWS Certified Solutions Architect - Professional SAP-C02", "sap-c02", "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-professional-sap-c02/view/", 529],
            ["AWS Certified Developer - Associate DVA-C02", "dva-c02", "https://www.examtopics.com/exams/amazon/aws-certified-developer-associate-dva-c02/view/", 557],
            ["Cloud Digital Leader", "gcp-cdl", "https://www.examtopics.com/exams/google/cloud-digital-leader/view/", 289],
            ["az-900", "az-900", "https://www.examtopics.com/exams/microsoft/az-900/view/", 475],
            ["AWS Certified Data Engineer - Associate DEA-C01", "dea-c01", "https://www.examtopics.com/exams/amazon/aws-certified-data-engineer-associate-dea-c01/view/", 286],
            ["Professional Machine Learning Engineer", "gcp-mle", "https://www.examtopics.com/exams/google/professional-machine-learning-engineer/view/", 339],
            ["Professional Cloud Network Engineer", "gcp-cne", "https://www.examtopics.com/exams/google/professional-cloud-network-engineer/view/", 248],
            ["Professional Cloud DevOps Engineer", "gcp-cdoe", "https://www.examtopics.com/exams/google/professional-cloud-devops-engineer/view/", 202],
            ["AWS Certified SysOps Administrator - Associate", "soa-c02", "https://www.examtopics.com/exams/amazon/aws-certified-sysops-administrator-associate/view/", 478],
            ["cissp", "cissp", "https://www.examtopics.com/exams/isc/cissp/view/", 484],
            ["ccsp", "ccsp", "https://www.examtopics.com/exams/isc/ccsp/view/", 512],
            ["cisa", "cisa", "https://www.examtopics.com/exams/isaca/cisa/view/", 1823],
            ["cism", "cism", "https://www.examtopics.com/exams/isaca/cism/view/", 1250],
            ["pmp", "pmp", "https://www.examtopics.com/exams/pmi/pmp/view/", 1417],
            ["Professional Cloud Database Engineer", "gcp-pdbe", "https://www.examtopics.com/exams/google/professional-cloud-database-engineer/view/", 182],
            ["Professional Google Workspace Administrator", "gcp-pgwa", "https://www.examtopics.com/exams/google/professional-google-workspace-administrator/view/", 151],
            ["Professional Cloud Developer", "gcp-pcd", "https://www.examtopics.com/exams/google/professional-cloud-developer/view/", 379],
            ["AWS Certified AI Practitioner AIF-C01", "aif-c01", "https://www.examtopics.com/exams/amazon/aws-certified-ai-practitioner-aif-c01/view/", 334],
            ["sscp", "sscp", "https://www.examtopics.com/exams/isc/sscp/view/", 1074],
            ["AWS Certified Machine Learning Engineer - Associate MLA-C01", "mla-c01", "https://www.examtopics.com/exams/amazon/aws-certified-machine-learning-engineer-associate-mla-c01/view/", 226],
            ["tda-c01", "tda-c01", "https://www.examtopics.com/exams/tableau/tda-c01/view/", 214],
            ["tds-c01", "tds-c01", "https://www.examtopics.com/exams/tableau/tds-c01/view/", 126],
            ["sc-300", "sc-300", "https://www.examtopics.com/exams/microsoft/sc-300/view/", 441],
            ["sc-900", "sc-900", "https://www.examtopics.com/exams/microsoft/sc-900/view/", 229],
            ["Associate Google Workspace Administrator", "gcp-agwa", "https://www.examtopics.com/exams/google/associate-google-workspace-administrator/view/", 108],
            ["csa", "csa", "https://www.examtopics.com/exams/servicenow/csa/view/", 408],
            ["cis-rc", "cis-rc", "https://www.examtopics.com/exams/servicenow/cis-rc/view/", 278],
            ["cis-itsm", "cis-itsm", "https://www.examtopics.com/exams/servicenow/cis-itsm/view/", 232],
            ["cis-hr", "cis-hr", "https://www.examtopics.com/exams/servicenow/cis-hr/view/", 229],
            ["cis-discovery", "cis-discovery", "https://www.examtopics.com/exams/servicenow/cis-discovery/view/", 122],
            ["cis-csm", "cis-csm", "https://www.examtopics.com/exams/servicenow/cis-csm/view/", 284],
            ["sc-401", "sc-401", "https://www.examtopics.com/exams/microsoft/sc-401/view/", 254],
            ["ogea-103", "ogea-103", "https://www.examtopics.com/exams/the-open-group/ogea-103/view/", 135],
            ["Associate Data Practitioner", "gcp-adp", "https://www.examtopics.com/exams/google/associate-data-practitioner/view/", 103],
            ["cad", "cad", "https://www.examtopics.com/exams/servicenow/cad/view/", 192],
            ["Certified Machine Learning Professional", "db-mlp", "https://www.examtopics.com/exams/databricks/certified-machine-learning-professional/view/", 60],
            ["Certified Machine Learning Associate", "db-mla", "https://www.examtopics.com/exams/databricks/certified-machine-learning-associate/view/", 74],
            ["Certified Generative AI Engineer Associate", "db-gaiea", "https://www.examtopics.com/exams/databricks/certified-generative-ai-engineer-associate/view/", 80],
            ["200-301", "200-301", "https://www.examtopics.com/exams/cisco/200-301/view/", 1395],
            #["Google Generative AI Leader", "https://www.examtopics.com/exams/google/generative-ai-leader/view/", 48],
            ["ms-102", "ms-102", "https://www.examtopics.com/exams/microsoft/ms-102/view/", 416],
            ["Certified Data Engineer Professional", "db-dep", "https://www.examtopics.com/exams/databricks/certified-data-engineer-professional/view/", 327],
            ["AWS Certified CloudOps Engineer - Associate SOA-C03", "soa-c03", "https://www.examtopics.com/exams/amazon/aws-certified-cloudops-engineer-associate-soa-c03/view/", 75],
            ["AWS Certified Generative AI Developer - Professional AIP-C01", "aip-c01", "https://www.examtopics.com/exams/amazon/aws-certified-generative-ai-developer-professional-aip-c01/view/", 85],
            ["cis-df", "cis-df", "https://www.examtopics.com/exams/servicenow/cis-df/view/", 75]]

# exams = [
#             ["https://www.examtopics.com/exams/amazon/aws-certified-data-analytics-specialty/view/",130]
#         ]
# pl-600
#exam_url = "https://www.examtopics.com/exams/microsoft/pl-600/view/"
#exam_name = 'pl-600-new'
#num_of_total_question = 255
#exam_name_str = 'pl-600'
#exam_name_for_search = 'PL-600'

# pl-200
#exam_url = "https://www.examtopics.com/exams/microsoft/pl-200/view/"
#exam_name = 'pl-200-new'
#num_of_total_question = 318
#exam_name_str = 'pl-200'

# clf-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/"
#exam_name = 'clf-c01-new'
#num_of_total_question = 988
#exam_name_str = 'clf-c01'

# clf-c02
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner-clf-c02/view/"
#exam_name = 'clf-c02-new'
#num_of_total_question = 719
#exam_name_str = 'clf-c02'

# ai-102
#exam_url = "https://www.examtopics.com/exams/microsoft/ai-102/view/"
#exam_name = 'ai-102-new'
#num_of_total_question = 333
#exam_name_str = 'ai-102'

# az-900
#exam_url = "https://www.examtopics.com/exams/microsoft/az-900/view/"
#exam_name = 'az-900-new'
#num_of_total_question = 475
#exam_name_str = 'az-900'

# ai-900
#exam_url = "https://www.examtopics.com/exams/microsoft/ai-900/view/"
#exam_name = 'ai-900-new'
#num_of_total_question = 246
#exam_name_str = 'ai-900'

# az-500
#exam_url = "https://www.examtopics.com/exams/microsoft/az-500/view/"
#exam_name = 'az-500-new'
#num_of_total_question = 505
#exam_name_str = 'az-500'

# # sap-c02-01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-professional/view/"
#exam_name = 'sap-c02-new'
#num_of_total_question = 1019
#exam_name_str = 'sap-c02'

# # sap-c02
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-professional-sap-c02/view/"
#exam_name = 'sap-c02-new'
#num_of_total_question = 529
#exam_name_str = 'sap-c02'

# ms-101
#exam_url = "https://www.examtopics.com/exams
# /microsoft/ms-101/view/"
#exam_name = 'ms-101-new'
#num_of_total_question = 437
#exam_name_str = 'ms-101'

# ms-102
#exam_url = "https://www.examtopics.com/exams/microsoft/ms-102/view/"
#exam_name = 'ms-102-new'
#num_of_total_question = 416
#exam_name_str = 'ms-102'
#exam_name_for_search = 'MS-102'

#sc-200
#exam_url = "https://www.examtopics.com/exams/microsoft/sc-200/view/"
#exam_name = 'sc-200-new'
#num_of_total_question = 389
#exam_name_str = 'sc-200'

#sc-300
#exam_url = "https://www.examtopics.com/exams/microsoft/sc-300/view/"
#exam_name = 'sc-300-new'
#num_of_total_question = 441
#exam_name_str = 'sc-300'
#exam_name_for_search = 'SC-300'

#gcp-agwa
#exam_url = "https://www.examtopics.com/exams/google/associate-google-workspace-administrator/view/"
#exam_name = 'gcp-agwa-new'
#num_of_total_question = 108
#exam_name_str = 'gcp-agwa'

#dop-c02
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-devops-engineer-professional-dop-c02/view/"
#exam_name = 'dop-c02-new'
#num_of_total_question = 418
#exam_name_str = 'dop-c02'
#exam_name_for_search = 'DOP-C02'

# # saa-c02
# exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate-saa-c02/view/"
# exam_name = 'saa-c02'
# num_of_total_question = 574
# num_of_question_per_page = 10

#scs-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-security-specialty/view/"
#exam_name = 'scs-c01-new'
#num_of_total_question = 509
#exam_name_str = 'scs-c01'

#scs-c02
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-security-specialty-scs-c02/view/"
#exam_name = 'scs-c02-new'
#num_of_total_question = 307
#exam_name_str = 'scs-c02'

#scs-c03
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-security-specialty-scs-c03/view/"
#exam_name = 'scs-c03-new'
#num_of_total_question = 62
#exam_name_str = 'scs-c03'

# # dva-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-developer-associate/view/"
#exam_name = 'dva-c01-new'
#num_of_total_question = 443
#exam_name_str = 'dva-c01'

# dva-c02
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-developer-associate-dva-c02/view/"
#exam_name = 'dva-c02-new'
#num_of_total_question = 557
#exam_name_str = 'dva-c02'

#az-104
#exam_url = "https://www.examtopics.com/exams/microsoft/az-104/view/"
#exam_name = 'az-104-new'
#num_of_total_question = 606
#exam_name_str = 'az-104'

#az-204
#exam_url = "https://www.examtopics.com/exams/microsoft/az-204/view/"
#exam_name = 'az-204-new'
#num_of_total_question = 487
#exam_name_str = 'az-204'
#exam_name_for_search = 'AZ-204'

# dp-100
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-100/view/"
#exam_name = 'dp-100-new'
#num_of_total_question = 527
#exam_name_str = 'dp-100'

# dp-300
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-300/view/"
#exam_name = 'dp-300-new'
#num_of_total_question = 373
#exam_name_str = 'dp-300'

# dp-203
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-203/view/"
#exam_name = 'dp-203-new'
#num_of_total_question = 389
#exam_name_str = 'dp-203'

# dp-500
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-500/view/"
#exam_name = 'dp-500-new'
#num_of_total_question = 194
#exam_name_str = 'dp-500'

# dp-600
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-600/view/"
#exam_name = 'dp-600-new'
#num_of_total_question = 198
#exam_name_str = 'dp-600'

# dp-700
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-700/view/"
#exam_name = 'dp-700-new'
#num_of_total_question = 118
#exam_name_str = 'dp-700'

# new_rca_file_title = "DP-203 Revised Correct Answers (修正的正确答案)\n\n"
# old_rca_file_name = 'DP-203 Revised Correct Answers.txt'
# old_qai_file_name = 'question_answer_index_dp-203.csv'
# new_qai_file_name = 'question_answer_index_dp-203-new.csv'
# new_rca_file_name = 'DP-203 Revised Correct Answers-New.txt'
# rca_log_name = "DP-203 Revised Correct Answers.log"

# ans-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-advanced-networking-specialty-ans-c01/view/"
#exam_name = 'ans-c01-new'
#num_of_total_question = 272
#exam_name_str = 'ans-c01'

#md-100
#exam_url = "https://www.examtopics.com/exams/microsoft/md-100/view/"
#exam_name = 'md-100-new'
#num_of_total_question = 412
#exam_name_str = 'md-100'

#az-400
#exam_url = "https://www.examtopics.com/exams/microsoft/az-400/view/"
#exam_name = 'az-400-new'
#num_of_total_question = 564
#exam_name_str = 'az-400'

#dbs-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-database-specialty/view/"
#exam_name = 'dbs-c01-new'
#num_of_total_question = 359
#exam_name_str = 'dbs-c01'

#soa-c02
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-sysops-administrator-associate/view/"
#exam_name = 'soa-c02-new'
#num_of_total_question = 478
#exam_name_str = 'soa-c02'

# pl-400
#exam_url = "https://www.examtopics.com/exams/microsoft/pl-400/view/"
#exam_name = 'pl-400-new'
#num_of_total_question = 429
#exam_name_str = 'pl-400'
#exam_name_for_search = 'PL-400'

# az-700
#exam_url = "https://www.examtopics.com/exams/microsoft/az-700/view/"
#exam_name = 'az-700-new'
#num_of_total_question = 369
#exam_name_str = 'az-700'
#exam_name_for_search = 'AZ-700'

# az-800
#exam_url = "https://www.examtopics.com/exams/microsoft/az-800/view/"
#exam_name = 'az-800-new'
#num_of_total_question = 292
#exam_name_str = 'az-800'
#exam_name_for_search = 'AZ-800'

# pl-300
#exam_url = "https://www.examtopics.com/exams/microsoft/pl-300/view/"
#exam_name = "pl-300-new"
#num_of_total_question = 371
#exam_name_str = 'pl-300'

# pl-900
#exam_url = "https://www.examtopics.com/exams/microsoft/pl-900/view/"
#exam_name = "pl-900-new"
#num_of_total_question = 351
#exam_name_str = 'pl-900'

# ms-900
#exam_url = "https://www.examtopics.com/exams/microsoft/ms-900/view/"
#exam_name = "ms-900-new"
#num_of_total_question = 507
#exam_name_str = 'ms-900'

# das-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-data-analytics-specialty/view/"
#exam_name = "das-c01-new"
#num_of_total_question = 164
#exam_name_str = 'das-c01'

# gcp-pca
#exam_url = "https://www.examtopics.com/exams/google/professional-cloud-architect/view/"
#exam_name = "gcp-pca-new"
#num_of_total_question = 346
#exam_name_str = 'gcp-pca'

# gcp-ace
#exam_url = "https://www.examtopics.com/exams/google/associate-cloud-engineer/view/"
#exam_name = "gcp-ace-new"
#num_of_total_question = 336
#exam_name_str = 'gcp-ace'

# gcp-mle
#exam_url = "https://www.examtopics.com/exams/google/professional-machine-learning-engineer/view/"
#exam_name = "gcp-mle-new"
#num_of_total_question = 339
#exam_name_str = 'gcp-mle'

# gcp-cdoe
#exam_url = "https://www.examtopics.com/exams/google/professional-cloud-devops-engineer/view/"
#exam_name = "gcp-cdoe-new"
#num_of_total_question = 202
#exam_name_str = 'gcp-cdoe'

# saa-c03
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate-saa-c03/view/"
#exam_name = "saa-c03-new"
#num_of_total_question = 1019
#exam_name_str = 'saa-c03'

# new_rca_file_title = "GCP-ACE Revised Correct Answers (修正的正确答案)\n\n"
# old_rca_file_name = 'CLF-C01 Revised Correct Answers.txt'
# old_qai_file_name = 'question_answer_index_gcp-ace.csv'
# new_qai_file_name = 'question_answer_index_gcp-ace-new.csv'
# new_rca_file_name = 'GCP-ACE Revised Correct Answers-New.txt'
# rca_log_name = "GCP-ACE Revised Correct Answers.log"


# ms-100
# exam_url = "https://www.examtopics.com/exams/microsoft/ms-100/view/"
# exam_name = "ms-100-new"
# num_of_total_question = 361

# mb-210
# exam_url = "https://www.examtopics.com/exams/microsoft/mb-210/view/"
# exam_name = "mb-210-new"
# num_of_total_question = 250


# dp-900
#exam_url = "https://www.examtopics.com/exams/microsoft/dp-900/view/"
#exam_name = "dp-900-new"
#num_of_total_question = 314
#exam_name_str = 'dp-900'
#exam_name_for_search = 'DP-900'


# az-305
#exam_url = "https://www.examtopics.com/exams/microsoft/az-305/view/"
#exam_name = "az-305-new"
#num_of_total_question = 286
#exam_name_str = 'az-305'

# mb-230
# exam_url = "https://www.examtopics.com/exams/microsoft/mb-230/view/"
# exam_name = "mb-230-new"
# num_of_total_question = 192

# mb-260
#exam_url = "https://www.examtopics.com/exams/microsoft/mb-260/view/"
#exam_name = "mb-260-new"
#num_of_total_question = 144
#exam_name_str = 'mb-260'


# pl-100
#exam_url = "https://www.examtopics.com/exams/microsoft/pl-100/view/"
#exam_name = "pl-100-new"
#num_of_total_question = 281
#exam_name_str = 'pl-100'

# google cloud digital leader
#exam_url = "https://www.examtopics.com/exams/google/cloud-digital-leader/view/"
#exam_name = "gcp-cdl-new"
#num_of_total_question = 289
#exam_name_str = 'gcp-cdl'

# gcp-cne
#exam_url = "https://www.examtopics.com/exams/google/professional-cloud-network-engineer/view/"
#exam_name = "gcp-cne-new"
#num_of_total_question = 248
#exam_name_str = 'gcp-cne'

# sc-100
#exam_url = "https://www.examtopics.com/exams/microsoft/sc-100/view/"
#exam_name = "sc-100-new"
#num_of_total_question = 173
#exam_name_str = 'sc-100'

# sc-900
#exam_url = "https://www.examtopics.com/exams/microsoft/sc-900/view/"
#exam_name = "sc-900-new"
#num_of_total_question = 229
#exam_name_str = 'sc-900'
#exam_name_for_search = 'SC-900'

# gcp-pde
#exam_url = "https://www.examtopics.com/exams/google/professional-data-engineer/view/"
#exam_name = "gcp-pde-new"
#num_of_total_question = 338
#exam_name_str = 'gcp-pde'

# mls-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-machine-learning-specialty/view/"
#exam_name = "mls-c01-new"
#num_of_total_question = 369
#exam_name_str = 'mls-c01'

# dea-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-data-engineer-associate-dea-c01/view/"
#exam_name = "dea-c01-new"
#num_of_total_question = 286
#exam_name_str = 'dea-c01'

# cgrc
#exam_url = "https://www.examtopics.com/exams/isc/cgrc/view/"
#exam_name = 'cgrc-pp-new'
#num_of_total_question = 500
#exam_name_str = 'cgrc-pp'

# csslp
#exam_url = "https://www.examtopics.com/exams/isc/csslp/view/"
#exam_name = 'csslp-pp-new'
#num_of_total_question = 500
#exam_name_str = 'csslp-pp'

# cissp
#exam_url = "https://www.examtopics.com/exams/isc/cissp/view/"
#exam_name = 'cissp-pp-new'
#num_of_total_question = 1000
#exam_name_str = 'cissp-pp'

# ccsp
#exam_url = "https://www.examtopics.com/exams/isc/ccsp/view/"
#exam_name = 'ccsp-pp-new'
#num_of_total_question = 1498
#exam_name_str = 'ccsp-pp'

# cisa
#exam_url = "https://www.examtopics.com/exams/isaca/cisa/view/"
#exam_name = 'cisa-new'
#num_of_total_question = 1823
#exam_name_str = 'cisa'

# cism
#exam_url = "https://www.examtopics.com/exams/isaca/cism/view/"
#exam_name = 'cism-new'
#num_of_total_question = 1250
#exam_name_str = 'cism'

# cc
#exam_url = "https://www.examtopics.com/exams/isc/cc/view/"
#exam_name = 'cc-pp-new'
#num_of_total_question = 500
#exam_name_str = 'cc-pp'

# pmp
#exam_url = "https://www.examtopics.com/exams/pmi/pmp/view/"
#exam_name = 'pmp-new'
#num_of_total_question = 1417
#exam_name_str = 'pmp'

# gcp-pdbe
#exam_url = "https://www.examtopics.com/exams/google/professional-cloud-database-engineer/view/"
#exam_name = 'gcp-pdbe-new'
#num_of_total_question = 182
#exam_name_str = 'gcp-pdbe'
#exam_name_for_search = 'Professional Cloud Database Engineer'

# gcp-pgwa
#exam_url = "https://www.examtopics.com/exams/google/professional-google-workspace-administrator/view/"
#exam_name = 'gcp-pgwa-new'
#num_of_total_question = 151
#exam_name_str = 'gcp-pgwa'

# gcp-pcd
#exam_url = "https://www.examtopics.com/exams/google/professional-cloud-developer/view/"
#exam_name = 'gcp-pcd-new'
#num_of_total_question = 379
#exam_name_str = 'gcp-pcd'
#exam_name_for_search = 'Professional Cloud Developer'

# aif-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-ai-practitioner-aif-c01/view/"
#exam_name = 'aif-c01-new'
#num_of_total_question = 334
#exam_name_str = 'aif-c01'
#exam_name_for_search = 'AWS Certified AI Practitioner AIF-C01'

# tda-c01
#exam_url = "https://www.examtopics.com/exams/tableau/tda-c01/view/"
#exam_name = 'tda-c01-new'
#num_of_total_question = 214
#exam_name_str = 'tda-c01'

# tds-c01
#exam_url = "https://www.examtopics.com/exams/tableau/tds-c01/view/"
#exam_name = 'tds-c01-new'
#num_of_total_question = 126
#exam_name_str = 'tds-c01'

# sscp
#exam_url = "https://www.examtopics.com/exams/isc/sscp/view/"
#exam_name = 'sscp-pp-new'
#num_of_total_question = 500
#exam_name_str = 'sscp-pp'

# crisc
#exam_url = "https://www.examtopics.com/exams/isaca/crisc/view/"
#exam_name = 'crisc-new'
#num_of_total_question = 1896
#exam_name_str = 'crisc'

# mla-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-machine-learning-engineer-associate-mla-c01/view/"
#exam_name = 'mla-c01-new'
#num_of_total_question = 226
#exam_name_str = 'mla-c01'
#exam_name_for_search = 'AWS Certified Machine Learning Engineer - Associate MLA-C01'

# sc-100-eh
#exam_url = "https://examheist.com/papers/microsoft/sc-100/"
#eh_exam_name = 'sc-100'
#exam_name = 'sc-100-eh-new'
#num_of_total_question = 311
#exam_name_str = 'sc-100-eh'

# ms-102-eh
#exam_url = "https://examheist.com/papers/microsoft/ms-102/"
#eh_exam_name = 'ms-102'
#exam_name = 'ms-102-eh-new'
#num_of_total_question = 428
#exam_name_str = 'ms-102-eh'

# csa
#exam_url = "https://www.examtopics.com/exams/servicenow/csa/view/"
#exam_name = 'csa-new'
#num_of_total_question = 408
#exam_name_str = 'csa'

# cis-rc
#exam_url = "https://www.examtopics.com/exams/servicenow/cis-rc/view/"
#exam_name = 'cis-rc-new'
#num_of_total_question = 278
#exam_name_str = 'cis-rc'
#exam_name_for_search = 'CIS-RC'

# cis-itsm
#exam_url = "https://www.examtopics.com/exams/servicenow/cis-itsm/view/"
#exam_name = 'cis-itsm-new'
#num_of_total_question = 232
#exam_name_str = 'cis-itsm'

# cis-hr
#exam_url = "https://www.examtopics.com/exams/servicenow/cis-hr/view/"
#exam_name = 'cis-hr-new'
#num_of_total_question = 229
#exam_name_str = 'cis-hr'

# cis-df
exam_url = "https://www.examtopics.com/exams/servicenow/cis-df/view/"
exam_name = 'cis-df-new'
num_of_total_question = 75
exam_name_str = 'cis-df'

# cis-discovery
#exam_url = "https://www.examtopics.com/exams/servicenow/cis-discovery/view/"
#exam_name = 'cis-discovery-new'
#num_of_total_question = 122
#exam_name_str = 'cis-discovery'
#exam_name_for_search = 'CIS-Discovery'

# cis-csm
#exam_url = "https://www.examtopics.com/exams/servicenow/cis-csm/view/"
#exam_name = 'cis-csm-new'
#num_of_total_question = 284
#exam_name_str = 'cis-csm'

# sc-401
#exam_url = "https://www.examtopics.com/exams/microsoft/sc-401/view/"
#exam_name = 'sc-401-new'
#num_of_total_question = 254
#exam_name_str = 'sc-401'
#exam_name_for_search = 'SC-401'

# ogea-103
#exam_url = "https://www.examtopics.com/exams/the-open-group/ogea-103/view/"
#exam_name = 'ogea-103-new'
#num_of_total_question = 135
#exam_name_str = 'ogea-103'

# gcp-adp
#exam_url = "https://www.examtopics.com/exams/google/associate-data-practitioner/view/"
#exam_name = 'gcp-adp-new'
#num_of_total_question = 103
#exam_name_str = 'gcp-adp'
#search_exam_name = 'Associate Data Practitioner'

# cad
#exam_url = "https://www.examtopics.com/exams/servicenow/cad/view/"
#exam_name = 'cad-new'
#num_of_total_question = 192
#exam_name_str = 'cad'

# db-mlp
#exam_url = "https://www.examtopics.com/exams/databricks/certified-machine-learning-professional/view/"
#exam_name = 'db-mlp-new'
#num_of_total_question = 60
#exam_name_str = 'db-mlp'

# db-mla
#exam_url = "https://www.examtopics.com/exams/databricks/certified-machine-learning-associate/view/"
#exam_name = 'db-mla-new'
#num_of_total_question = 74
#exam_name_str = 'db-mla'

# db-gaiea
#exam_url = "https://www.examtopics.com/exams/databricks/certified-generative-ai-engineer-associate/view/"
#exam_name = 'db-gaiea-new'
#num_of_total_question = 80
#exam_name_str = 'db-gaiea'

# db-dep
#exam_url = "https://www.examtopics.com/exams/databricks/certified-data-engineer-professional/view/"
#exam_name = 'db-dep-new'
#num_of_total_question = 327
#exam_name_str = 'db-dep'

# gcp-pcse-eh
#exam_url = "https://examheist.com/papers/google/professional-cloud-security-engineer/"
#eh_exam_name = 'professional-cloud-security-engineer'
#exam_name = 'gcp-pcse-eh-new'
#num_of_total_question = 366
#exam_name_str = 'gcp-pcse-eh'

# gh-300-eh
#exam_url = "https://examheist.com/exam/microsoft/gh-300/"
#eh_exam_name = 'gh-300'
#exam_name = 'gh-300-eh-new'
#num_of_total_question = 129
#exam_name_str = 'gh-300-eh'

# cisco-200-301
#exam_url = "https://www.examtopics.com/exams/cisco/200-301/view/"
#exam_name = '200-301-new'
#num_of_total_question = 1395
#exam_name_str = '200-301'

# gcp-gail
#exam_url = "https://www.examtopics.com/exams/google/generative-ai-leader/view/"
#exam_name = 'gcp-gail-new'
#num_of_total_question = 48
#exam_name_str = 'gcp-gail'

# gcp-gail-eh
#exam_url = "https://examheist.com/papers/google/generative-ai-leader/"
#eh_exam_name = 'generative-ai-leader'
#exam_name = 'gcp-gail-eh-new'
#num_of_total_question = 137
#exam_name_str = 'gcp-gail-eh'

# 350-401
#exam_url = "https://www.examtopics.com/exams/cisco/350-401/view/"
#exam_name = '350-401-new'
#num_of_total_question = 1066
#exam_name_str = '350-401'

# az-140
#exam_url = "https://www.examtopics.com/exams/microsoft/az-140/view/"
#exam_name = 'az-140-new'
#num_of_total_question = 330
#exam_name_str = 'az-140'
#exam_name_for_search = 'AZ-140'

# SOA-C03
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-cloudops-engineer-associate-soa-c03/view/"
#exam_name = 'soa-c03-new'
#num_of_total_question = 75
#exam_name_str = 'soa-c03'

# aip-c01
#exam_url = "https://www.examtopics.com/exams/amazon/aws-certified-generative-ai-developer-professional-aip-c01/view/"
#exam_name = 'aip-c01-new'
#num_of_total_question = 85
#exam_name_str = 'aip-c01'

# og0-091
#exam_url = "https://www.examtopics.com/exams/the-open-group/og0-091/view/"
#exam_name = 'og0-091-new'
#num_of_total_question = 313
#exam_name_str = 'og0-091'

# og0-093
#exam_url = "https://www.examtopics.com/exams/the-open-group/og0-093/view/"
#exam_name = 'og0-093-new'
#num_of_total_question = 417
#exam_name_str = 'og0-093'

# new_rca_file_title = "MLS-C01 Revised Correct Answers (修正的正确答案)\n\n"
# old_rca_file_name = 'MLS-C01 Revised Correct Answers.txt'
# old_qai_file_name = 'question_answer_index_mls-c01.csv'
# new_qai_file_name = 'question_answer_index_mls-c01-new.csv'
# new_rca_file_name = 'MLS-C01 Revised Correct Answers-New.txt'
# rca_log_name = "MLS-C01 Revised Correct Answers.log"

# old_rca_file_name = 'SCS-C01 Revised Correct Answers.txt'
old_rca_file_name = exam_name_str.upper() + ' Revised Correct Answers.txt'
old_qai_file_name = 'question_answer_index_' + exam_name_str + '.csv'
new_rca_file_title = exam_name_str.upper() + " Revised Correct Answers (修正的正确答案)\n\n"
new_rca_file_name = exam_name_str.upper() + ' Revised Correct Answers-New.txt'
new_qai_file_name = 'question_answer_index_' + exam_name + '.csv'
rca_log_name = exam_name_str.upper() + " Revised Correct Answers.log"

# old_qai_file_name = 'question_answer_index_sap-c01-1.csv'
# new_qai_file_name = 'question_answer_index_sap-c01-2.csv'
# old_rca_file_name = 'SAP-C01 Revised Correct Answers.txt'