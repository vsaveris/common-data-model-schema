# Microsoft Common Data Model Schema Extraction, in python
Script (`cdm.py`) implements a class for schema extraction from Microsoft CDM (json) files. The script extracts pairs of attribute names and types for the input cdm.json file.

## Prerequisites
Microsoft Common Data Model (CDM) Schema files https://github.com/microsoft/CDM.git

## Components
The implementation is in python. The repository includes the below source files:
```
cdm.py  : Common Data Model Schema Extraction class.
test.py : Example usage code of the Common Data Model Schema Extraction class.
```

## Execution Examples
The below examples assume that the CDM files (reference [1]) are stored in the ./CDM relevant path.

## Example 1: Sales -> Opportunity (version 1.0) Schema Extraction
```
$python test.py ./CDM/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/sales/Opportunity.1.0.cdm.json ./CDM/schemaDocuments/core/ ./CDM/schemaDocuments/core/applicationCommon/

CDM class, path = ./CDM/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/sales/Opportunity.1.0.cdm.json, core_path = ./CDM/schemaDocuments/core/, base_path = ./CDM/schemaDocuments/core/applicationCommon/
Document ID: {'entityName': 'Opportunity', 'extendsEntity': 'CdsStandard', 'versionNumber': '1.0'}

Read attributes of the core_entity = CdsStandard
- Core file path: ./CDM/schemaDocuments/core/wellKnownCDSAttributeGroups.1.0.cdm.json
- Attributes: ['cdsCreationModificationDatesAndIds', 'cdsOwnershipInfo', 'cdsTimeZoneInfo', 'cdsVersionTracking']
- Parsing members of cdsCreationModificationDatesAndIds
- Parsing members of cdsOwnershipInfo
- Parsing members of cdsTimeZoneInfo
- Parsing members of cdsVersionTracking

Read attributes of the document, parsing members.

Number of attributes in the schema Opportunity, version 1.0: 121
  1. createdOn                       : dateTime
  2. createdby                       : userId
  3. modifiedOn                      : dateTime
  4. modifiedby                      : userId
  5. createdonbehalfby               : userId
  6. modifiedonbehalfby              : userId
  7. overriddenCreatedOn             : dateTime
  8. importSequenceNumber            : integer
  9. ownerid                         : entityId
 10. ownerIdType                     : entityName
 11. owningbusinessunit              : entityId
 12. owninguser                      : userId
 13. owningteam                      : entityId
 14. timeZoneRuleVersionNumber       : integer
 15. UTCConversionTimeZoneCode       : integer
 16. versionNumber                   : cdsVersionNumber
 17. opportunityId                   : entityId
 18. emailAddress                    : email
 19. name                            : name
 20. processId                       : guid
 21. stageId                         : guid
 22. traversedPath                   : string
 23. actualCloseDate                 : dateTime
 24. actualValue                     : currency
 25. transactioncurrencyid           : entityId
 26. exchangeRate                    : decimal
 27. actualValueBase                 : baseCurrency
 28. budgetAmount                    : currency
 29. budgetAmountBase                : baseCurrency
 30. budgetStatus                    : listLookup
 31. budgetStatus_display            : localizedDisplayText
 32. closeProbability                : integer
 33. completeInternalReview          : boolean
 34. confirmInterest                 : boolean
 35. currentSituation                : string
 36. customerid                      : entityId
 37. customerIdType                  : entityName
 38. customerNeed                    : string
 39. customerPainPoints              : string
 40. decisionMaker                   : boolean
 41. description                     : string
 42. developProposal                 : boolean
 43. discountAmount                  : currency
 44. discountAmountBase              : baseCurrency
 45. discountPercentage              : decimal
 46. estimatedCloseDate              : dateTime
 47. estimatedValue                  : currency
 48. estimatedValueBase              : baseCurrency
 49. evaluateFit                     : boolean
 50. resolveFeedback                 : boolean
 51. fileDebrief                     : boolean
 52. completeFinalProposal           : boolean
 53. finalDecisionDate               : dateTime
 54. freightAmount                   : currency
 55. freightAmountBase               : baseCurrency
 56. initialCommunication            : listLookup
 57. initialCommunication_display    : localizedDisplayText
 58. isRevenueSystemCalculated       : boolean
 59. need                            : listLookup
 60. need_display                    : localizedDisplayText
 61. opportunityRatingCode           : listLookup
 62. opportunityRatingCode_display   : localizedDisplayText
 63. parentaccountid                 : entityId
 64. parentcontactid                 : entityId
 65. participatesInWorkflow          : boolean
 66. pricelevelid                    : entityId
 67. pricingErrorCode                : listLookup
 68. pricingErrorCode_display        : localizedDisplayText
 69. priorityCode                    : listLookup
 70. priorityCode_display            : localizedDisplayText
 71. purchaseProcess                 : listLookup
 72. purchaseProcess_display         : localizedDisplayText
 73. purchaseTimeFrame               : listLookup
 74. purchaseTimeFrame_display       : localizedDisplayText
 75. salesStage                      : listLookup
 76. salesStage_display              : localizedDisplayText
 77. salesStageCode                  : listLookup
 78. salesStageCode_display          : localizedDisplayText
 79. presentProposal                 : boolean
 80. captureProposalFeedback         : boolean
 81. proposedSolution                : string
 82. pursuitDecision                 : boolean
 83. qualificationComments           : string
 84. quoteComments                   : string
 85. sendThankYouNote                : boolean
 86. scheduleFollowupProspect        : dateTime
 87. scheduleFollowUpQualify         : dateTime
 88. scheduleProposalMeeting         : dateTime
 89. stateCode                       : listLookup
 90. stateCode_display               : localizedDisplayText
 91. statusCode                      : listLookup
 92. statusCode_display              : localizedDisplayText
 93. stepId                          : guid
 94. stepName                        : name
 95. timeLine                        : listLookup
 96. timeLine_display                : localizedDisplayText
 97. totalAmount                     : currency
 98. totalAmountBase                 : baseCurrency
 99. totalAmountLessFreight          : currency
100. totalAmountLessFreightBase      : baseCurrency
101. totalDiscountAmount             : currency
102. totalDiscountAmountBase         : baseCurrency
103. totalLineItemAmount             : currency
104. totalLineItemAmountBase         : baseCurrency
105. totalLineItemDiscountAmount     : currency
106. totalLineItemDiscountAmountBase : baseCurrency
107. totalTax                        : currency
108. totalTaxBase                    : baseCurrency
109. identifyCustomerContacts        : boolean
110. identifyCompetitors             : boolean
111. identifyPursuitTeam             : boolean
112. presentFinalProposal            : boolean
113. onHoldTime                      : integer
114. lastOnHoldTime                  : dateTime
115. slaid                           : entityId
116. slainvokedid                    : entityId
117. timeSpentByMeOnEmailAndMeetings : email
118. originatingleadid               : entityId
119. accountId                       : entityId
120. contactId                       : entityId
121. campaignid                      : entityId
``` 

## Example 2: Crm -> Account (version 1.0) Schema Extraction
```
$python python test.py ./CDM/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/Account.1.0.cdm.json ./CDM/schemaDocuments/core/ ./CDM/schemaDocuments/core/applicationCommon/

CDM class, path = ./CDM/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/Account.1.0.cdm.json, core_path = ./CDM/schemaDocuments/core/, base_path = ./CDM/schemaDocuments/core/applicationCommon/
Document ID: {'entityName': 'Account', 'extendsEntity': 'base_Account/Account', 'versionNumber': '1.0'}

CDM class, path = ./CDM/schemaDocuments/core/applicationCommon/Account.1.0.cdm.json, core_path = ./CDM/schemaDocuments/core/, base_path = None
Document ID: {'entityName': 'Account', 'extendsEntity': 'CdsStandard', 'versionNumber': '1.0'}

Read attributes of the core_entity = CdsStandard
- Core file path: ./CDM/schemaDocuments/core/wellKnownCDSAttributeGroups.1.0.cdm.json
- Attributes: ['cdsCreationModificationDatesAndIds', 'cdsOwnershipInfo', 'cdsTimeZoneInfo', 'cdsVersionTracking']
- Parsing members of cdsCreationModificationDatesAndIds
- Parsing members of cdsOwnershipInfo
- Parsing members of cdsTimeZoneInfo
- Parsing members of cdsVersionTracking

Read attributes of the document, parsing members.

Read attributes of the document, parsing members.

Number of attributes in the schema Account, version 1.0: 123
  1. createdOn                            : dateTime
  2. createdby                            : userId
  3. modifiedOn                           : dateTime
  4. modifiedby                           : userId
  5. createdonbehalfby                    : userId
  6. modifiedonbehalfby                   : userId
  7. overriddenCreatedOn                  : dateTime
  8. importSequenceNumber                 : integer
  9. ownerid                              : entityId
 10. ownerIdType                          : entityName
 11. owningbusinessunit                   : entityId
 12. owninguser                           : userId
 13. owningteam                           : entityId
 14. timeZoneRuleVersionNumber            : integer
 15. UTCConversionTimeZoneCode            : integer
 16. versionNumber                        : cdsVersionNumber
 17. accountId                            : entityId
 18. accountCategoryCode                  : listLookup
 19. accountCategoryCode_display          : localizedDisplayText
 20. customerSizeCode                     : listLookup
 21. customerSizeCode_display             : localizedDisplayText
 22. preferredContactMethodCode           : listLookup
 23. preferredContactMethodCode_display   : localizedDisplayText
 24. customerTypeCode                     : listLookup
 25. customerTypeCode_display             : localizedDisplayText
 26. accountRatingCode                    : listLookup
 27. accountRatingCode_display            : localizedDisplayText
 28. industryCode                         : listLookup
 29. industryCode_display                 : localizedDisplayText
 30. territoryCode                        : listLookup
 31. territoryCode_display                : localizedDisplayText
 32. accountClassificationCode            : listLookup
 33. accountClassificationCode_display    : localizedDisplayText
 34. businessTypeCode                     : listLookup
 35. businessTypeCode_display             : localizedDisplayText
 36. traversedPath                        : string
 37. paymentTermsCode                     : listLookup
 38. paymentTermsCode_display             : localizedDisplayText
 39. shippingMethodCode                   : listLookup
 40. shippingMethodCode_display           : localizedDisplayText
 41. primarycontactid                     : entityId
 42. participatesInWorkflow               : boolean
 43. name                                 : name
 44. accountNumber                        : string
 45. revenue                              : currency
 46. numberOfEmployees                    : integer
 47. description                          : string
 48. SIC                                  : string
 49. ownershipCode                        : listLookup
 50. ownershipCode_display                : localizedDisplayText
 51. marketCap                            : currency
 52. sharesOutstanding                    : integer
 53. tickerSymbol                         : tickerSymbol
 54. stockExchange                        : string
 55. webSiteUrl                           : url
 56. ftpSiteUrl                           : url
 57. EMailAddress1                        : email
 58. EMailAddress2                        : email
 59. EMailAddress3                        : email
 60. doNotPhone                           : boolean
 61. doNotFax                             : boolean
 62. telephone1                           : phone
 63. doNotEMail                           : boolean
 64. telephone2                           : phone
 65. fax                                  : string
 66. telephone3                           : phone
 67. doNotPostalMail                      : boolean
 68. doNotBulkEMail                       : boolean
 69. doNotBulkPostalMail                  : boolean
 70. creditLimit                          : currency
 71. creditOnHold                         : boolean
 72. parentaccountid                      : entityId
 73. aging30                              : currency
 74. stateCode                            : listLookup
 75. stateCode_display                    : localizedDisplayText
 76. aging60                              : currency
 77. statusCode                           : listLookup
 78. statusCode_display                   : localizedDisplayText
 79. aging90                              : currency
 80. addressid                            : entityId
 81. preferredAppointmentDayCode          : listLookup
 82. preferredAppointmentDayCode_display  : localizedDisplayText
 83. preferredsystemuserid                : entityId
 84. preferredAppointmentTimeCode         : listLookup
 85. preferredAppointmentTimeCode_display : localizedDisplayText
 86. merged                               : boolean
 87. doNotSendMM                          : boolean
 88. masterid                             : entityId
 89. lastUsedInCampaign                   : dateTime
 90. exchangeRate                         : decimal
 91. transactioncurrencyid                : entityId
 92. creditLimitBase                      : baseCurrency
 93. aging30Base                          : baseCurrency
 94. revenueBase                          : baseCurrency
 95. aging90Base                          : baseCurrency
 96. marketCapBase                        : baseCurrency
 97. aging60Base                          : baseCurrency
 98. yomiName                             : name
 99. stageId                              : guid
100. processId                            : guid
101. entityImageId                        : guid
102. timeSpentByMeOnEmailAndMeetings      : email
103. createdByExternalParty               : entityId
104. modifiedByExternalParty              : entityId
105. primarySatoriId                      : string
106. primaryTwitterId                     : string
107. slaid                                : entityId
108. slainvokedid                         : entityId
109. onHoldTime                           : integer
110. lastOnHoldTime                       : dateTime
111. followEmail                          : boolean
112. marketingOnly                        : boolean
113. originatingleadid                    : entityId
114. preferredequipmentid                 : entityId
115. preferredserviceid                   : entityId
116. territoryid                          : entityId
117. openDeals                            : integer
118. openDealsDate                        : dateTime
119. openDealsState                       : integer
120. openRevenue                          : currency
121. openRevenueBase                      : baseCurrency
122. openRevenueDate                      : dateTime
123. openRevenueState                     : integer
```

## Example 3: Sales -> Discount (version 1.0) Schema Extraction
```
$python test.py ./CDM/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/sales/Discount.1.0.cdm.json ./CDM/schemaDocuments/core/ ./CDM/schemaDocuments/core/applicationCommon/

CDM class, path = ./CDM/schemaDocuments/core/applicationCommon/foundationCommon/crmCommon/sales/Discount.1.0.cdm.json, core_path = ./CDM/schemaDocuments/core/, base_path = ./CDM/schemaDocuments/core/applicationCommon/
Document ID: {'entityName': 'Discount', 'extendsEntity': 'CdmEntity', 'versionNumber': '1.0'}

Read attributes of the core_entity = CdmEntity
- Core file path: ./CDM/schemaDocuments/core/wellKnownCDSAttributeGroups.1.0.cdm.json
- Attributes: None

Read attributes of the document, parsing members.

Number of attributes in the schema Discount, version 1.0: 25
 1. discountId                : entityId
 2. createdOn                 : dateTime
 3. createdby                 : entityId
 4. modifiedOn                : dateTime
 5. modifiedby                : entityId
 6. createdonbehalfby         : entityId
 7. modifiedonbehalfby        : entityId
 8. versionNumber             : bigInteger
 9. importSequenceNumber      : integer
10. overriddenCreatedOn       : dateTime
11. timeZoneRuleVersionNumber : integer
12. UTCConversionTimeZoneCode : integer
13. name                      : name
14. amount                    : currency
15. transactioncurrencyid     : entityId
16. exchangeRate              : decimal
17. amountBase                : baseCurrency
18. discounttypeid            : entityId
19. highQuantity              : decimal
20. isAmountType              : boolean
21. lowQuantity               : decimal
22. organizationId            : guid
23. percentage                : decimal
24. statusCode                : listLookup
25. statusCode_display        : localizedDisplayText
```

## System Requirements (Dependencies)
The script has been developed and verified in a **Python 3.7** environment. Installation details of python, can be found in the following link: [Python Installation](https://www.python.org/downloads/)

## References
1. [Microsoft Common Data Model (CDM) Schema](https://github.com/microsoft/CDM.git)
