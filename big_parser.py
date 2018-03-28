from pygeometa import render_template
import xmltodict
import os
import cfg

# with open('1.xml') as f:
    # dictxml = xmltodict.parse(f.read())



#===========================================================================================================================

#====================================  MD_Metadata  ============================================================================

#===========================================================================================================================

def parse_big_md(input_xml):
    dictxml = xmltodict.parse(input_xml)
    print dictxml
    print "                       "
    print "======================="
    print "Md_metadata            "
    print "======================="

    try:
        fileIdentifier = dictxml['gmd:MD_Metadata']['gmd:fileIdentifier']['gco:CharacterString']
        if fileIdentifier.strip() == None:
            fileIdentifier = 'Tidak Ada'
        print "fileIdentifier:", fileIdentifier
    except:
        fileIdentifier = 'Tidak Ada'
        print "Passed1 fileIdentifier"
    try:
        language = dictxml['gmd:MD_Metadata']['gmd:language']['gco:CharacterString']
        if language.strip() == None:
            language = 'Tidak Ada'
        print "language:", language
    except:
        language = 'Tidak Ada'
        print "Passed2  language"
    try:
        hierarchyLevel = dictxml['gmd:MD_Metadata']['gmd:hierarchyLevel']['gmd:MD_ScopeCode']
        if hierarchyLevel.strip() == None:
            hierarchyLevel = 'Tidak Ada'
        print "hierarchyLevel:", hierarchyLevel
    except:
        hierarchyLevel = 'Tidak Ada'
        print "Passed3 hierarchyLevel"
    try:
        hierarchyLevelName = dictxml['gmd:MD_Metadata']['gmd:hierarchyLevelName']['gco:CharacterString']
        if hierarchyLevelName.strip() == None:
            hierarchyLevelName = 'Tidak Ada'
        print "hierarchyLevelName:", hierarchyLevelName
    except:
        hierarchyLevelName = 'Tidak Ada'
        print "Passed4 hierarchyLevelName"        

    #===========================================================================================================================

    #====================================  CONTACT  ============================================================================

    #===========================================================================================================================
    print "                       "
    print "======================="
    print "  Contac               "
    print "======================="

    try:
        individualName = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:individualName']['gco:CharacterString']
        if individualName.strip() == None:
            individualName = 'Tidak Ada'
        print "individualName:", individualName
    except:
        individualName = 'Tidak Ada'
        print "Passed5 individualName"
    try:
        organisationName = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:organisationName']['gco:CharacterString']
        print "ORF:", organisationName
        if organisationname.strip() == None:
            organisationname='Tidak Ada'    
        print "organisationName:", organisationName
    except:
      organisationname ='Tidak Ada'
      print "Passed6 organisationName"
    try:
        positionName = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if positionName.strip() == None:
            positionName = 'Tidak Ada'
        print "positionName:", positionName
    except:
        positionName ='Tidak Ada'
        print "Passed61 positionName"
    try:
        voice = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:voice']['gco:CharacterString']
        if voice.strip() == None:
            voice = 'Tidak Ada'
        print "voice:", voice
    except:
      voice ='Tidak Ada'
      print "Passed7 voice"
    try:
        facsimile = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:facsimile']['gco:CharacterString']
        if facsimile.strip() == None:
            facsimile = "Tidak Ada"
        print "facsimile:", facsimile
    except:
      facsimile ='Tidak Ada'
      print "Passed8 facsimile"
    try:
        deliveryPoint = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:deliveryPoint']['gco:CharacterString']
        if deliveryPoint.strip() == None:
            deliveryPoint = "Tidak ada"
        print "deliveryPoint:", deliveryPoint
    except:
      deliveryPoint ='Tidak Ada'
      print "Passed9 deliveryPoint"
    try:
        city = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:city']['gco:CharacterString']
        if city.strip() == None:
            city = "Tidak ada"
        print "city:", city
    except:
      city ='Tidak Ada'
      print "Passed10 city"
    try:
        administrativeArea = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:administrativeArea']['gco:CharacterString']
        if administrativeArea.strip() == None:
            administrativeArea = "tidak ada"
        print "administrativeArea:", administrativeArea
    except:
      administrativeArea ='Tidak Ada'
      print "Passed11 administrativeArea"
    try:
        postalCode = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:postalCode']['gco:CharacterString']
        if postalCode.strip() == None:
            postalCode == "Tidak ada"
        print "postalCode:", postalCode
    except:
      postalCode ='Tidak Ada'
      print "Passed12 postalCode"
    try:
        country = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:country']['gco:CharacterString']
        if country.strip() == None:
            country = 'tidak ada'
        print "country:", country
    except:
      country ='Tidak Ada'
      print "Passed13 country"
    try:
        electronicMailAddress = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:electronicMailAddress']['gco:CharacterString']
        if electronicMailAddress.strip() == None:
            electronicMailAddress = 'tidak ada'
        print "electronicMailAddress:", electronicMailAddress
    except:
      electronicMailAddress ='Tidak Ada'
      print "Passed14 electronicMailAddress"

    try:
        linkagecontact = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:linkage']['gmd:URL']
        if linkagecontact.strip() == None:
            linkagecontact = 'tidak ada'
        print "linkagecontact:", linkagecontact
    except:
        linkagecontact ='Tidak Ada'
        print "Passed14 linkagecontact"
    try:
        namecontact = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:name']['gco:CharacterString']
        if namecontact.strip() == None:
            namecontact = 'tidak ada'
        print "namecontact:", namecontact
    except:
        namecontact ='Tidak Ada'
        print "Passed14 namecontact"
    try:
        descriptioncontact = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:description']['gco:CharacterString']
        if descriptioncontact.strip() == None:
            descriptioncontact = 'tidak ada'
        print "descriptioncontact:", descriptioncontact
    except:
        descriptioncontact ='Tidak Ada'
        print "Passed14 descriptioncontact"
    try:
        functioncontact = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:function']['gmd:CI_OnLineFunctionCode']
        if functioncontact.strip() == None:
            functioncontact = 'tidak ada'
        print "functioncontact:", functioncontact
    except:
        functioncontact ='Tidak Ada'
        print "Passed14 functioncontact"

    try:
        CI_RoleCode = dictxml['gmd:MD_Metadata']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:role']['gmd:CI_RoleCode']
        if CI_RoleCode.strip() == None:
            CI_RoleCode = 'tidak ada'
        print "CI_RoleCode:", CI_RoleCode
    except:
      CI_RoleCode ='Tidak Ada'
      print "Passed15 CI_RoleCode"	

    try:
        dateStamp = dictxml['gmd:MD_Metadata']['gmd:dateStamp']['gco:DateTime']
        if dateStamp.strip() == None:
            dateStamp = 'tidak ada'
        print "dateStamp:", dateStamp
    except:
      dateStamp = 'Tidak Ada'
      print "Passed16 dateStamp"
    try:
        metadataStandardName = dictxml['gmd:MD_Metadata']['gmd:metadataStandardName']['gco:CharacterString']
        if metadataStandardName.strip() == None:
            metadataStandardName = 'tidak ada'
        print "metadataStandardName:", metadataStandardName
    except:
        metadataStandardName = 'Tidak Ada'
        print "Passed161 metadataStandardName"      
    try:
        metadataStandardVersion = dictxml['gmd:MD_Metadata']['gmd:metadataStandardVersion']['gco:CharacterString']
        if metadataStandardVersion.strip() == None:
            metadataStandardVersion = 'tidak ada'
        print "metadataStandardVersion:", metadataStandardName
    except:
        metadataStandardName = 'Tidak Ada'
        print "Passed162 metadataStandardVersion"
    try:
        dataSetURI = dictxml['gmd:MD_Metadata']['gmd:dataSetURI']['gco:CharacterString']
        if dataSetURI.strip() == None:
            dataSetURI = 'tidak ada'
        print "dataSetURI:", dataSetURI
    except:
        dataSetURI = 'Tidak Ada'
        print "Passed163 dataSetURI"
    #===========================================================================================================================================================================================================

    #===================================================================  spatialRepresentationInfo plural ===========================================================================================================

    #===========================================================================================================================================================================================================
    print "                       "
    print "======================="
    print "  spatialRepresentationInfo               "
    print "======================="

    try:
        dimensionName = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][0]['gmd:AbstractMD_SpatialRepresentation']['gmd:axisDimensionProperties']['gmd:MD_Dimension']['gmd:dimensionName']['gmd:MD_DimensionNameTypeCode']
        if dimensionName.strip() == None:
            dimensionName = 'tidak ada'
        print "dimensionName:", dimensionName
    except:
      dimensionName = 'Tidak Ada'
      print "Passed17 dimensionName"
    try:
        dimensionSize = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][0]['gmd:AbstractMD_SpatialRepresentation']['gmd:axisDimensionProperties']['gmd:MD_Dimension']['gmd:dimensionSize']['gco:Integer']
        if dimensionSize.strip() == None:
            dimensionSize = 'tidak ada'
        print "dimensionSize:", dimensionSize
    except:
      dimensionSize = 'Tidak Ada'
      print "Passed18 dimensionSize"
    try:
        resolution = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][0]['gmd:AbstractMD_SpatialRepresentation']['gmd:axisDimensionProperties']['gmd:MD_Dimension']['gmd:resolution']['gco:Measure']
        if resolution.strip() == None:
            resolution = 'tidak ada'
        print "resolution:", resolution
    except:
      resolution = 'Tidak Ada'
      print "Passed19 resolution"		
    try:
        topologyLevel = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][1]['gmd:AbstractMD_SpatialRepresentation']['gmd:topologyLevel']['gmd:MD_TopologyLevelCode']
        if topologyLevel.strip() == None:
            topologyLevel = 'tidak ada'
        print "topologyLevel:", topologyLevel
    except:
        topologyLevel = 'Tidak Ada'
        print "Passed191 topologyLevel"
    try:
        geometricObjectType = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][1]['gmd:AbstractMD_SpatialRepresentation']['gmd:geometricObjects']['gmd:MD_GeometricObjects']['gmd:geometricObjectType']['gmd:MD_GeometricObjectTypeCode']
        if geometricObjectType.strip() == None:
            geometricObjectType = 'tidak ada'
        print "geometricObjectType:", geometricObjectType
    except:
        geometricObjectType = 'Tidak Ada'
        print "Passed192 geometricObjectType"
    try:
        geometricObjectCount = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][1]['gmd:AbstractMD_SpatialRepresentation']['gmd:geometricObjects']['gmd:MD_GeometricObjects']['gmd:geometricObjectCount']['gco:Integer']
        if geometricObjectCount.strip() == None:
            geometricObjectCount = 'tidak ada'
        print "geometricObjectCount:", geometricObjectCount
    except:
        geometricObjectCount = 'Tidak Ada'
        print "Passed193 geometricObjectCount"
    try:
        checkPointAvailability = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][2]['gmd:AbstractMD_SpatialRepresentation']['gmd:checkPointAvailability']['gco:Boolean']
        if checkPointAvailability.strip() == None:
            checkPointAvailability = 'tidak ada'
        print "checkPointAvailability:", checkPointAvailability
    except:
        checkPointAvailability = 'Tidak Ada'
        print "Passed194 checkPointAvailability"  
    try:
        checkPointDescription = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][2]['gmd:AbstractMD_SpatialRepresentation']['gmd:checkPointDescription']['gco:CharacterString']
        if checkPointDescription.strip() == None:
            checkPointDescription = 'Tidak Ada'
        print "checkPointDescription:", checkPointDescription
    except:
        checkPointDescription  = 'Tidak Ada'
        print "Passed195 checkPointDescription"
    try:
        controlPointAvailability = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][3]['gmd:AbstractMD_SpatialRepresentation']['gmd:controlPointAvailability']['gco:Boolean']
        if controlPointAvailability.strip() == None:
            controlPointAvailability = 'tidak ada'
        print "controlPointAvailability:", controlPointAvailability
    except:
        controlPointAvailability = 'Tidak Ada'
        print "Passed196 controlPointAvailability"
    try:
        orientationParameterDescription = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][3]['gmd:AbstractMD_SpatialRepresentation']['gmd:orientationParameterDescription']['gco:CharacterString']
        if orientationParameterDescription.strip() == None:
            orientationParameterDescription = 'tidak ada'
        print "orientationParameterDescription:", orientationParameterDescription
    except:    
        orientationParameterDescription = 'Tidak Ada'
        print "Passed197 orientationParameterDescription"
    try:
        titlegeoreferenceable = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][3]['gmd:AbstractMD_SpatialRepresentation']['gmd:parameterCitation']['gmd:CI_Citation']['gmd:title']['gco:CharacterString']
        if titlegeoreferenceable.strip() == None:
            titlegeoreferenceable = 'tidak ada'
        print "titlegeoreferenceable:", titlegeoreferenceable
    except:    
        titlegeoreferenceable = 'Tidak Ada'
        print "Passed198 titlegeoreferenceable"
    try:
        dategeoreferenceable = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][3]['gmd:AbstractMD_SpatialRepresentation']['gmd:parameterCitation']['gmd:CI_Citation']['gmd:date']['gmd:CI_Date']['gmd:date']['gco:DateTime']
        if dategeoreferenceable.strip() == None:
            dategeoreferenceable = 'tidak ada'
        print "dategeoreferenceable:", dategeoreferenceable
    except:    
        dategeoreferenceable = 'Tidak Ada'
        print "Passed199 dategeoreferenceable"    
    try:
        editiongeoreferenceable = dictxml['gmd:MD_Metadata']['gmd:spatialRepresentationInfo'][3]['gmd:AbstractMD_SpatialRepresentation']['gmd:parameterCitation']['gmd:CI_Citation']['gmd:edition']['gco:CharacterString']
        if editiongeoreferenceable.strip() == None:
            editiongeoreferenceable = 'tidak ada'
        print "editiongeoreferenceable:", editiongeoreferenceable
    except:    
        editiongeoreferenceable = 'Tidak Ada'
        print "Passed1991 editiongeoreferenceable"


    #===========================================================================================================================================================================================================

    #===================================================================  referenceSystemInfo  plural ===========================================================================================================

    #===========================================================================================================================================================================================================

    print "                       "
    print "======================="
    print "  referenceSystemInfo               "
    print "======================="

    try:
        code = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][0]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:code']['gco:CharacterString']
        if code.strip() == None:
            code = 'tidak ada'
        print "code:", code
    except:
      code = 'Tidak Ada'
      print "Passed20 code"	
    try:
        codeSpace = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][0]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:codeSpace']['gco:CharacterString']
        if codeSpace.strip() == None:
            codeSpace = 'tidak ada'
        print "codeSpace:", codeSpace
    except:
      codeSpace = 'Tidak Ada'
      print "Passed21 codeSpace"
    try:
        version = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][0]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:version']['gco:CharacterString']
        if version.strip() == None:
            version = 'tidak ada'
        print "version:", version
    except:
      version = 'Tidak Ada'
      print "Passed22 version"


    try:
        code1 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][1]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:code']['gco:CharacterString']
        if code1.strip() == None:
            code1 = 'tidak ada'
        print "code1:", code1
    except:
        code1 = 'Tidak Ada'
        print "Passed221 code1"   
    try:
        codeSpace1 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][1]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:codeSpace']['gco:CharacterString']
        if codeSpace1.strip() == None:
            codeSpace1 = 'tidak ada'
        print "codeSpace1:", codeSpace1
    except:
        codeSpace1 = 'Tidak Ada'
        print "Passed222 codeSpace1"
    try:
        version1 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][1]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:version']['gco:CharacterString']
        if version1.strip() == None:
            version1 = 'tidak ada'
        print "version1:", version1
    except:
        version1 = 'Tidak Ada'
        print "Passed223 version1"


    try:
        code2 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][2]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:code']['gco:CharacterString']
        if code2.strip() == None:
            code2 = 'tidak ada'
        print "code2:", code2
    except:
        code2 = 'Tidak Ada'
        print "Passed224 code"   
    try:
        codeSpace2 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][2]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:codeSpace']['gco:CharacterString']
        if codeSpace2.strip() == None:
            codeSpace2 = 'tidak ada'
        print "codeSpace2:", codeSpace2
    except:
        codeSpace2 = 'Tidak Ada'
        print "Passed225 codeSpace2"
    try:
        version2 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][2]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:version']['gco:CharacterString']
        if version2.strip() == None:
            version2 = 'tidak ada'
        print "version2:", version2
    except:
        version2 = 'Tidak Ada'
        print "Passed226 version2"


    try:
        code3 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][3]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:code']['gco:CharacterString']
        if code3.strip() == None:
            code3 = 'tidak ada'
        print "code3:", code3
    except:
        code3 = 'Tidak Ada'
        print "Passed227 code3"   
    try:
        codeSpace3 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][3]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:codeSpace']['gco:CharacterString']
        if codeSpace3.strip() == None:
            codeSpace3 = 'tidak ada'
        print "codeSpace3:", codeSpace3
    except:
        codeSpace3 = 'Tidak Ada'
        print "Passed228 codeSpace3"
    try:
        version3 = dictxml['gmd:MD_Metadata']['gmd:referenceSystemInfo'][3]['gmd:MD_ReferenceSystem']['gmd:referenceSystemIdentifier']['gmd:RS_Identifier']['gmd:version']['gco:CharacterString']
        if version3.strip() == None:
            version3 = 'tidak ada'
        print "version3:", version3
    except:
        version3 = 'Tidak Ada'
        print "Passed229 version3"

    #===========================================================================================================================================================================================================

    #===================================================================  identificationInfo  ===========================================================================================================

    #===========================================================================================================================================================================================================

    print "                       "
    print "======================="
    print "  identificationInfo               "
    print "======================="

    try:
        title = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:title']['gco:CharacterString']
        if title.strip() == None:
            title = 'tidak ada'
        print "title:", title
    except:
      title = 'Tidak Ada title'
      print "Passed23"
    try:
        alternateTitle = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:alternateTitle']['gco:CharacterString']
        if alternateTitle.strip() == None:
            alternateTitle = 'tidak ada'
        print "alternateTitle:", alternateTitle
    except:
      alternateTitle = 'Tidak Ada'
      print "Passed24 alternateTitle"
    try:
        date = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:date']['gmd:CI_Date']['gmd:date']['gco:DateTime']
        if date.strip() == None:
            date = 'tidak ada'
        print "date:", date
    except:
      date = 'tidak ada'
      print "Passed25 date"
    try:
        edition = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:edition']['gco:CharacterString']
        if edition.strip() == None:
            edition = 'tidak ada'
        print "edition:", edition
    except:
      edition = 'Tidak Ada'
      print "Passed26 edition"

    try:
        individualNameIdentifi = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:individualName']['gco:CharacterString']
        if individualNameIdentifi.strip() == None:
            individualNameIdentifi = 'tidak ada'
        print "individualNameIdentifi:", individualNameIdentifi
    except:
        individualNameIdentifi = 'Tidak Ada'
        print "Passed261 individualNameIdentifi"
    try:
        organisationNameIdentifi = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:organisationName']['gco:CharacterString']
        if organisationNameIdentifi.strip() == None:
            organisationNameIdentifi = 'tidak ada'
        print "organisationNameIdentifi:", organisationNameIdentifi
    except:
        organisationNameIdentifi = 'Tidak Ada'
        print "Passed261 organisationNameIdentifi"
    try:
        positionNameIdentifi = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if positionNameIdentifi.strip() == None:
            positionNameIdentifi = 'tidak ada'
        print "positioNameIdentifi:", positionNameIdentifi
    except:
        positionNameIdentifi = 'Tidak Ada'
        print "Passed262 positionNameIdentifi"
    try: 
        voiceIdentifi = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:citation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if voiceIdentifi.strip() == None:
            voiceIdentifi = 'tidak ada'
        print "voiceIdentifi:", voiceIdentifi
    except:
        voiceIdentifi = 'Tidak Ada'
        print "Passed262 voiceIdentifi"



    try:   
        abstract = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:abstract']['gco:CharacterString'].replace('\n','').replace('?','')
        if abstract.strip() == None:
            abstract = 'tidak ada'
        print "abstract:", abstract
    except:
      abstract = 'Tidak Ada'
      print "Passed27 abstract"

    try:   
        purpose = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:purpose']['gco:CharacterString']
        if purpose.strip() == None:
            purpose = 'tidak ada'
        print "purpose:", purpose
    except:
        purpose = 'Tidak Ada'
        print "Passed27 purpose"

    try:   
        credit = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:credit']['gco:CharacterString']
        if credit.strip() == None:
            credit = 'tidak ada'
        print "credit:", credit
    except:
        credit = 'Tidak Ada'
        print "Passed27 credit"

    try:   
        status = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:status']['gmd:MD_ProgressCode']
        if status.strip() == None:
            status = 'tidak ada'
        print "status:", status
    except:
        status = 'Tidak Ada'
        print "Passed27 status"

    try:   
        individualNameidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:individualName']['gco:CharacterString']
        if individualNameidentifi2.strip() == None:
            individualNameidentifi2 = 'tidak ada'
        print "individualNameidentifi2:", individualNameidentifi2
    except:
        individualNameidentifi2 = 'Tidak Ada'
        print "Passed27 individualNameidentifi2"

    try:   
        organisationNameidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:organisationName']['gco:CharacterString']
        if organisationNameidentifi2.strip() == None:
            organisationNameidentifi2 = 'tidak ada'
        print "organisationNameidentifi2:", organisationNameidentifi2
    except:
        organisationNameidentifi2 = 'Tidak Ada'
        print "Passed27 organisationNameidentifi2"

    try:   
        positionNameidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if positionNameidentifi2.strip() == None:
            positionNameidentifi2 = 'tidak ada'
        print "positionNameidentifi2:", positionNameidentifi2
    except:
        positionNameidentifi2 = 'Tidak Ada'
        print "Passed27 positionNameidentifi2"

    try:   
        voiceidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:voice']['gco:CharacterString']
        if voiceidentifi2.strip() == None:
            voiceidentifi2 = 'tidak ada'
        print "voiceidentifi2:", voiceidentifi2
    except:
        voiceidentifi2 = 'Tidak Ada'
        print "Passed27 voiceidentifi2"

    try:   
        facsimileidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:facsimile']['gco:CharacterString']
        if facsimileidentifi2.strip() == None:
            facsimileidentifi2 = 'tidak ada'
        print "facsimileidentifi2:", facsimileidentifi2
    except:
        facsimileidentifi2 = 'Tidak Ada'
        print "Passed27 facsimileidentifi2"

    try:   
        deliveryPointidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:deliveryPoint']['gco:CharacterString']
        if deliveryPointidentifi2.strip() == None:
            deliveryPointidentifi2 = 'tidak ada'
        print "deliveryPointidentifi2:", deliveryPointidentifi2
    except:
        deliveryPointidentifi2 = 'Tidak Ada'
        print "Passed27 deliveryPointidentifi2"

    try:   
        cityidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:city']['gco:CharacterString']
        if cityidentifi2.strip() == None:
            cityidentifi2 = 'tidak ada'
        print "cityidentifi2:", cityidentifi2
    except:
        cityidentifi2 = 'Tidak Ada'
        print "Passed27 cityidentifi2"

    try:   
        administrativeAreaidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:administrativeArea']['gco:CharacterString']
        if administrativeAreaidentifi2.strip() == None:
            administrativeAreaidentifi2 = 'tidak ada'
        print "administrativeAreaidentifi2:", administrativeAreaidentifi2
    except:
        administrativeAreaidentifi2 = 'Tidak Ada'
        print "Passed27 administrativeAreaidentifi2"

    try:   
        postalCodeidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:postalCode']['gco:CharacterString']
        if postalCodeidentifi2.strip() == None:
            postalCodeidentifi2 = 'tidak ada'
        print "postalCodeidentifi2:", postalCodeidentifi2
    except:
        postalCodeidentifi2 = 'Tidak Ada'
        print "Passed27 postalCodeidentifi2"

    try:   
        countryidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:country']['gco:CharacterString']
        if countryidentifi2.strip() == None:
            countryidentifi2 = 'tidak ada'
        print "countryidentifi2:", countryidentifi2
    except:
        countryidentifi2 = 'Tidak Ada'
        print "Passed27 countryidentifi2"

    try:   
        electronicMailAddressidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:electronicMailAddress']['gco:CharacterString']
        if electronicMailAddressidentifi2.strip() == None:
            electronicMailAddressidentifi2 = 'tidak ada'
        print "electronicMailAddressidentifi2:", electronicMailAddressidentifi2
    except:
        electronicMailAddressidentifi2 = 'Tidak Ada'
        print "Passed27 electronicMailAddressidentifi2"

    try:   
        linkageidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:linkage']['gmd:URL']
        if linkageidentifi2.strip() == None:
            linkageidentifi2 = 'tidak ada'
        print "linkageidentifi2:", linkageidentifi2
    except:
        linkageidentifi2 = 'Tidak Ada'
        print "Passed27 linkageidentifi2"

    try:   
        protocolidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:protocol']['gco:CharacterString']
        if protocolidentifi2.strip() == None:
            protocolidentifi2 = 'tidak ada'
        print "protocolidentifi2:", protocolidentifi2
    except:
        protocolidentifi2 = 'Tidak Ada'
        print "Passed27 protocolidentifi2"

    try:   
        applicationProfileidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:applicationProfile']['gco:CharacterString']
        if applicationProfileidentifi2.strip() == None:
            applicationProfileidentifi2 = 'tidak ada'
        print "applicationProfileidentifi2:", applicationProfileidentifi2
    except:
        applicationProfileidentifi2 = 'Tidak Ada'
        print "Passed27 applicationProfileidentifi2"


    try:   
        nameidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:name']['gco:CharacterString']
        if nameidentifi2.strip() == None:
            nameidentifi2 = 'tidak ada'
        print "nameidentifi2:", nameidentifi2
    except:
        nameidentifi2 = 'Tidak Ada'
        print "Passed27 nameidentifi2"


    try:   
        descriptionidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:description']['gco:CharacterString']
        if descriptionidentifi2.strip() == None:
            descriptionidentifi2 = 'tidak ada'
        print "descriptionidentifi2:", descriptionidentifi2
    except:
        descriptionidentifi2 = 'Tidak Ada'
        print "Passed27 descriptionidentifi2"


    try:   
        functionidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:function']['gco:CharacterString']
        if functionidentifi2.strip() == None:
            functionidentifi2 = 'tidak ada'
        print "functionidentifi2:", functionidentifi2
    except:
        functionidentifi2 = 'Tidak Ada'
        print "Passed27 functionidentifi2"


    try:   
        hoursOfServiceidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:hoursOfService']['gco:CharacterString']
        if hoursOfServiceidentifi2.strip() == None:
            hoursOfServiceidentifi2 = 'tidak ada'
        print "hoursOfServiceidentifi2:", hoursOfServiceidentifi2
    except:
        hoursOfServiceidentifi2 = 'Tidak Ada'
        print "Passed27 hoursOfServiceidentifi2"

    try:   
        contactInstructionsidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:contactInstructions']['gco:CharacterString']
        if contactInstructionsidentifi2.strip() == None:
            contactInstructionsidentifi2 = 'tidak ada'
        print "contactInstructionsidentifi2:", contactInstructionsidentifi2
    except:
        contactInstructionsidentifi2 = 'Tidak Ada'
        print "Passed27 contactInstructionsidentifi2"


    try:   
        CI_RoleCodeidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:pointOfContact']['gmd:CI_ResponsibleParty']['gmd:role']['gmd:CI_RoleCode']
        if CI_RoleCodeidentifi2.strip() == None:
            CI_RoleCodeidentifi2 = 'tidak ada'
        print "CI_RoleCodeidentifi2:", CI_RoleCodeidentifi2
    except:
        CI_RoleCodeidentifi2 = 'Tidak Ada'
        print "Passed27 CI_RoleCodeidentifi2"


    try:   
        maintenanceAndUpdateFrequencyidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:maintenanceAndUpdateFrequency']['gmd:MD_MaintenanceFrequencyCode']
        if maintenanceAndUpdateFrequencyidentifi2.strip() == None:
            maintenanceAndUpdateFrequencyidentifi2 = 'tidak ada'
        print "maintenanceAndUpdateFrequencyidentifi2:", maintenanceAndUpdateFrequencyidentifi2
    except:
        maintenanceAndUpdateFrequencyidentifi2 = 'Tidak Ada'
        print "Passed27 maintenanceAndUpdateFrequencyidentifi2"

    try:   
        dateOfNextUpdateidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:dateOfNextUpdate']['gco:DateTime']
        if dateOfNextUpdateidentifi2.strip() == None:
            dateOfNextUpdateidentifi2 = 'tidak ada'
        print "dateOfNextUpdateidentifi2:", dateOfNextUpdateidentifi2
    except:
        dateOfNextUpdateidentifi2 = 'Tidak Ada'
        print "Passed27 dateOfNextUpdateidentifi2"

    try:   
        userDefinedMaintenanceFrequencyidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:userDefinedMaintenanceFrequency']['gts:TM_PeriodDuration']
        if userDefinedMaintenanceFrequencyidentifi2.strip() == None:
            userDefinedMaintenanceFrequencyidentifi2 = 'tidak ada'
        print "userDefinedMaintenanceFrequencyidentifi2:", userDefinedMaintenanceFrequencyidentifi2
    except:
        userDefinedMaintenanceFrequencyidentifi2 = 'Tidak Ada'
        print "Passed27 userDefinedMaintenanceFrequencyidentifi2"

    try:   
        updateScopeidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:updateScope']['gmd:MD_ScopeCode']
        if updateScopeidentifi2.strip() == None:
            updateScopeidentifi2 = 'tidak ada'
        print "updateScopeidentifi2:", updateScopeidentifi2
    except:
        updateScopeidentifi2 = 'Tidak Ada'
        print "Passed27 updateScopeidentifi2"


    try:   
        maintenanceNoteidentifi2 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:maintenanceNote']['gco:CharacterString']
        if maintenanceNoteidentifi2.strip() == None:
            maintenanceNoteidentifi2 = 'tidak ada'
        print "maintenanceNoteidentifi2:", maintenanceNoteidentifi2
    except:
        maintenanceNoteidentifi2 = 'Tidak Ada'
        print "Passed27 maintenanceNoteidentifi2"


    try:   
        individualNameidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:individualName']['gco:CharacterString']
        if individualNameidentifi3.strip() == None:
            individualNameidentifi3 = 'tidak ada'
        print "individualNameidentifi3:", individualNameidentifi3
    except:
        individualNameidentifi3 = 'Tidak Ada'
        print "Passed27 individualNameidentifi3"

    try:   
        organisationNameidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:organisationName']['gco:CharacterString']
        if organisationNameidentifi3.strip() == None:
            organisationNameidentifi3 = 'tidak ada'
        print "organisationNameidentifi3:", organisationNameidentifi3
    except:
        organisationNameidentifi3 = 'Tidak Ada'
        print "Passed27 organisationNameidentifi3"


    try:   
        positionNameNameidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if positionNameNameidentifi3.strip() == None:
            positionNameNameidentifi3 = 'tidak ada'
        print "positionNameNameidentifi3:", positionNameNameidentifi3
    except:
        positionNameNameidentifi3 = 'Tidak Ada'
        print "Passed27 positionNameNameidentifi3"

    try:   
        voiceidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:voice']['gco:CharacterString']
        if voiceidentifi3.strip() == None:
            voiceidentifi3 = 'tidak ada'
        print "voiceidentifi3:", voiceidentifi3
    except:
        voiceidentifi3 = 'Tidak Ada'
        print "Passed27 voiceidentifi3"

    try:   
        facsimileidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:facsimile']['gco:CharacterString']
        if facsimileidentifi3.strip() == None:
            facsimileidentifi3 = 'tidak ada'
        print "facsimileidentifi3:", facsimileidentifi3
    except:
        facsimileidentifi3 = 'Tidak Ada'
        print "Passed27 facsimileidentifi3"

    try:   
        deliveryPointidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:deliveryPoint']['gco:CharacterString']
        if deliveryPointidentifi3.strip() == None:
            deliveryPointidentifi3 = 'tidak ada'
        print "deliveryPointidentifi3:", deliveryPointidentifi3
    except:
        deliveryPointidentifi3 = 'Tidak Ada'
        print "Passed27 deliveryPointidentifi3"


    try:   
        cityidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:city']['gco:CharacterString']
        if cityidentifi3.strip() == None:
            cityidentifi3 = 'tidak ada'
        print "cityidentifi3:", cityidentifi3
    except:
        cityidentifi3 = 'Tidak Ada'
        print "Passed27 cityidentifi3"

    try:   
        administrativeAreaidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:administrativeArea']['gco:CharacterString']
        if administrativeAreaidentifi3.strip() == None:
            administrativeAreaidentifi3 = 'tidak ada'
        print "administrativeAreaidentifi3:", administrativeAreaidentifi3
    except:
        administrativeAreaidentifi3 = 'Tidak Ada'
        print "Passed27 administrativeAreaidentifi3"

    try:   
        postalCodeidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:postalCode']['gco:CharacterString']
        if postalCodeidentifi3.strip() == None:
            postalCodeidentifi3 = 'tidak ada'
        print "postalCodeidentifi3:", postalCodeidentifi3
    except:
        postalCodeidentifi3 = 'Tidak Ada'
        print "Passed27 postalCodeidentifi3"

    try:   
        countryidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:country']['gco:CharacterString']
        if countryidentifi3.strip() == None:
            countryidentifi3 = 'tidak ada'
        print "countryidentifi3:", countryidentifi3
    except:
        countryidentifi3 = 'Tidak Ada'
        print "Passed27 countryidentifi3"    

    try:   
        electronicMailAddressidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:electronicMailAddress']['gco:CharacterString']
        if electronicMailAddressidentifi3.strip() == None:
            electronicMailAddressidentifi3 = 'tidak ada'
        print "electronicMailAddressidentifi3:", electronicMailAddressidentifi3
    except:
        electronicMailAddressidentifi3 = 'Tidak Ada'
        print "Passed27 electronicMailAddressidentifi3"

    try:   
        linkageidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:linkage']['gmd:URL']
        if linkageidentifi3.strip() == None:
            linkageidentifi3 = 'tidak ada'
        print "linkageidentifi3:", linkageidentifi3
    except:
        linkageidentifi3 = 'Tidak Ada'
        print "Passed27 linkageidentifi3"

    try:   
        protocolidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:protocol']['gco:CharacterString']
        if protocolidentifi3.strip() == None:
            protocolidentifi3 = 'tidak ada'
        print "protocolidentifi3:", protocolidentifi3
    except:
        protocolidentifi3 = 'Tidak Ada'
        print "Passed27 protocolidentifi3"


    try:   
        applicationProfileidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:applicationProfile']['gco:CharacterString']
        if applicationProfileidentifi3.strip() == None:
            applicationProfileidentifi3 = 'tidak ada'
        print "applicationProfileidentifi3:", applicationProfileidentifi3
    except:
        applicationProfileidentifi3 = 'Tidak Ada'
        print "Passed27 applicationProfileidentifi3"

    try:   
        nameidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:name']['gco:CharacterString']
        if nameidentifi3.strip() == None:
            nameidentifi3 = 'tidak ada'
        print "nameidentifi3:", nameidentifi3
    except:
        nameidentifi3 = 'Tidak Ada'
        print "Passed27 nameidentifi3"

    try:   
        descriptionidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:description']['gco:CharacterString']
        if descriptionidentifi3.strip() == None:
            descriptionidentifi3 = 'tidak ada'
        print "descriptionidentifi3:", descriptionidentifi3
    except:
        descriptionidentifi3 = 'Tidak Ada'
        print "Passed27 descriptionidentifi3"    

    try:   
        functionidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:function']['md:CI_OnLineFunctionCode']
        if functionidentifi3.strip() == None:
            functionidentifi3 = 'tidak ada'
        print "functionidentifi3:", functionidentifi3
    except:
        functionidentifi3 = 'Tidak Ada'
        print "Passed27 functionidentifi3"    


    try:   
        hoursOfServiceidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:hoursOfService']['gco:CharacterString']
        if hoursOfServiceidentifi3.strip() == None:
            hoursOfServiceidentifi3 = 'tidak ada'
        print "hoursOfServiceidentifi3:", hoursOfServiceidentifi3
    except:
        hoursOfServiceidentifi3 = 'Tidak Ada'
        print "Passed27 hoursOfServiceidentifi3"  

    try:   
        contactInstructionsidentifi3 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:contactInstructions']['gco:CharacterString']
        if contactInstructionsidentifi3.strip() == None:
            contactInstructionsidentifi3 = 'tidak ada'
        print "contactInstructionsidentifi3:", contactInstructionsidentifi3
    except:
        contactInstructionsidentifi3 = 'Tidak Ada'
        print "Passed27 contactInstructionsidentifi3"  




    try:   
        roleidentifi3= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceMaintenance']['gmd:MD_MaintenanceInformation']['gmd:contact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:']['gmd:CI_RoleCode']
        if roleidentifi3.strip() == None:
            roleidentifi3= 'tidak ada'
        print "roleidentifi3:", roleidentifi3
    except:
        roleidentifi3= 'Tidak Ada'
        print "Passed27 roleidentifi3" 

    try:   
        filenameidentifi3= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:graphicOverview']['gmd:MD_BrowseGraphic']['gmd:fileName']['gco:CharacterString']
        if filenameidentifi3.strip() == None:
            filenameidentifi3= 'tidak ada'
        print "filenameidentifi3:", filenameidentifi3
    except:
        filenameidentifi3= 'Tidak Ada'
        print "Passed27 filenameidentifi3" 

    try:   
        fileDescriptionidentifi3= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:graphicOverview']['gmd:MD_BrowseGraphic']['gmd:fileDescriptionident']['gco:CharacterString']
        if fileDescriptionidentifi3.strip() == None:
            fileDescriptionidentifi3= 'tidak ada'
        print "fileDescriptionidentifi3:", fileDescriptionidentifi3
    except:
        fileDescriptionidentifi3= 'Tidak Ada'
        print "Passed27 fileDescriptionidentifi3"

    try:   
        fileTypeidentifi3= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:graphicOverview']['gmd:MD_BrowseGraphic']['gmd:fileType']['gco:CharacterString']
        if fileTypeidentifi3.strip() == None:
            fileTypeidentifi3= 'tidak ada'
        print "fileTypeidentifi3:", fileTypeidentifi3
    except:
        fileTypeidentifi3= 'Tidak Ada'
        print "Passed27 fileTypeidentifi3"


    try:   
        amendmentNumber = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:amendmentNumber']['gco:CharacterString']
        if amendmentNumber.strip() == None:
            amendmentNumber = 'tidak ada'
        print "amendmentNumber:", amendmentNumber
    except:
        amendmentNumber = 'Tidak Ada'
        print "Passed27 amendmentNumber"


    try:   
        fileDecompressionTechnique = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:fileDecompressionTechnique']['gco:CharacterString']
        if fileDecompressionTechnique.strip() == None:
            fileDecompressionTechnique = 'tidak ada'
        print "fileDecompressionTechnique:", fileDecompressionTechnique
    except:
        fileDecompressionTechnique = 'Tidak Ada'
        print "Passed27 fileDecompressionTechnique"

    try:   
        individualNameidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:individualName']['gco:CharacterString']
        if individualNameidentifi7.strip() == None:
            individualNameidentifi7 = 'tidak ada'
        print "individualNameidentifi7:", individualNameidentifi7
    except:
        individualNameidentifi7 = 'Tidak Ada'
        print "Passed27 individualNameidentifi7"

    try:   
        organisationNameidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:organisationName']['gco:CharacterString']
        if organisationNameidentifi7.strip() == None:
            organisationNameidentifi7 = 'tidak ada'
        print "organisationNameidentifi7:", organisationNameidentifi7
    except:
        organisationNameidentifi7 = 'Tidak Ada'
        print "Passed27 organisationNameidentifi7"

    try:   
        positionNameidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if positionNameidentifi7.strip() == None:
            positionNameidentifi7 = 'tidak ada'
        print "positionNameidentifi7:", positionNameidentifi7
    except:
        positionNameidentifi7 = 'Tidak Ada'
        print "Passed27 positionNameidentifi7"



    try:   
        voiceidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:voice']['gco:CharacterString']
        if voiceidentifi7.strip() == None:
            voiceidentifi7 = 'tidak ada'
        print "voiceidentifi7:", voiceidentifi7
    except:
        voiceidentifi7 = 'Tidak Ada'
        print "Passed27 voiceidentifi7"

    try:   
        facsimileidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:facsimile']['gco:CharacterString']
        if facsimileidentifi7.strip() == None:
            facsimileidentifi7 = 'tidak ada'
        print "facsimileidentifi7:", facsimileidentifi7
    except:
        facsimileidentifi7 = 'Tidak Ada'
        print "Passed27 facsimileidentifi7"



    try:   
        deliveryPointidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:deliveryPoint']['gco:CharacterString']
        if deliveryPointidentifi7.strip() == None:
            deliveryPointidentifi7 = 'tidak ada'
        print "deliveryPointidentifi7:", deliveryPointidentifi7
    except:
        deliveryPointidentifi7 = 'Tidak Ada'
        print "Passed27 deliveryPointidentifi7"

    try:   
        cityidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:city']['gco:CharacterString']
        if cityidentifi7.strip() == None:
            cityidentifi7 = 'tidak ada'
        print "cityidentifi7:", cityidentifi7
    except:
        cityidentifi7 = 'Tidak Ada'
        print "Passed27 cityidentifi7"

    try:   
        administrativeAreaidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:administrativeArea']['gco:CharacterString']
        if administrativeAreaidentifi7.strip() == None:
            administrativeAreaidentifi7 = 'tidak ada'
        print "administrativeAreaidentifi7:", administrativeAreaidentifi7
    except:
        administrativeAreaidentifi7 = 'Tidak Ada'
        print "Passed27 administrativeAreaidentifi7"

    try:   
        postalCodeidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:postalCode']['gco:CharacterString']
        if postalCodeidentifi7.strip() == None:
            postalCodeidentifi7 = 'tidak ada'
        print "postalCodeidentifi7:", postalCodeidentifi7
    except:
        postalCodeidentifi7 = 'Tidak Ada'
        print "Passed27 postalCodeidentifi7"

    try:   
        countryidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:country']['gco:CharacterString']
        if countryidentifi7.strip() == None:
            countryidentifi7 = 'tidak ada'
        print "countryidentifi7:", countryidentifi7
    except:
        countryidentifi7 = 'Tidak Ada'
        print "Passed27 countryidentifi7"

    try:   
        electronicMailAddressidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:electronicMailAddress']['gco:CharacterString']
        if electronicMailAddressidentifi7.strip() == None:
            electronicMailAddressidentifi7 = 'tidak ada'
        print "electronicMailAddressidentifi7:", electronicMailAddressidentifi7
    except:
        electronicMailAddressidentifi7 = 'Tidak Ada'
        print "Passed27 electronicMailAddressidentifi7"

    try:   
        linkageidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:linkage']['gco:CharacterString']
        if linkageidentifi7.strip() == None:
            linkageidentifi7 = 'tidak ada'
        print "linkageidentifi7:", linkageidentifi7
    except:
        linkageidentifi7 = 'Tidak Ada'
        print "Passed27 linkageidentifi7"

    try:   
        protocolidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:protocol']['gco:CharacterString']
        if protocolidentifi7.strip() == None:
            protocolidentifi7 = 'tidak ada'
        print "protocolidentifi7:", protocolidentifi7
    except:
        protocolidentifi7 = 'Tidak Ada'
        print "Passed27 protocolidentifi7"

    try:   
        applicationProfileidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:applicationProfile']['gco:CharacterString']
        if applicationProfileidentifi7.strip() == None:
            applicationProfileidentifi7 = 'tidak ada'
        print "applicationProfileidentifi7:", applicationProfileidentifi7
    except:
        applicationProfileidentifi7 = 'Tidak Ada'
        print "Passed27 applicationProfileidentifi7"


    try:   
        nameidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:name']['gco:CharacterString']
        if nameidentifi7.strip() == None:
            nameidentifi7 = 'tidak ada'
        print "nameidentifi7:", nameidentifi7
    except:
        nameidentifi7 = 'Tidak Ada'
        print "Passed27 nameidentifi7"

    try:   
        descriptionidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:description']['gco:CharacterString']
        if descriptionidentifi7.strip() == None:
            descriptionidentifi7 = 'tidak ada'
        print "descriptionidentifi7:", descriptionidentifi7
    except:
        descriptionidentifi7 = 'Tidak Ada'
        print "Passed27 descriptionidentifi7"    

    try:   
        functionidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:function']['gmd:CI_OnLineFunctionCode']
        if functionidentifi7.strip() == None:
            functionidentifi7 = 'tidak ada'
        print "functionidentifi7:", functionidentifi7
    except:
        functionidentifi7 = 'Tidak Ada'
        print "Passed27 functionidentifi7"

    try:   
        hoursOfServiceidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:hoursOfService']['gco:CharacterString']
        if hoursOfServiceidentifi7.strip() == None:
            hoursOfServiceidentifi7 = 'tidak ada'
        print "hoursOfServiceidentifi7:", hoursOfServiceidentifi7
    except:
        hoursOfServiceidentifi7 = 'Tidak Ada'
        print "Passed27 hoursOfServiceidentifi7"

    try:   
        contactInstructionsidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:contactInstructions']['gco:CharacterString']
        if contactInstructionsidentifi7.strip() == None:
            contactInstructionsidentifi7 = 'tidak ada'
        print "contactInstructionsidentifi7:", contactInstructionsidentifi7
    except:
        contactInstructionsidentifi7 = 'Tidak Ada'
        print "Passed27 contactInstructionsidentifi7"

    try:   
        roleidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorContact']['gmd:CI_ResponsibleParty']['gmd:role']['gmd:CI_RoleCode']
        if roleidentifi7.strip() == None:
            roleidentifi7 = 'tidak ada'
        print "roleidentifi7:", roleidentifi7
    except:
        roleidentifi7 = 'Tidak Ada'
        print "Passed27 roleidentifi7"    

    try:   
        feesidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributionOrderProcess']['gmd:MD_StandardOrderProcess']['gmd:fees']['gco:CharacterString']
        if feesidentifi7.strip() == None:
            feesidentifi7 = 'tidak ada'
        print "feesidentifi7:", feesidentifi7
    except:
        feesidentifi7 = 'Tidak Ada'
        print "Passed27 feesidentifi7"

    try:   
        plannedAvailableDateTimeidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributionOrderProcess']['gmd:MD_StandardOrderProcess']['gmd:plannedAvailableDateTime']['gco:DateTime']
        if plannedAvailableDateTimeidentifi7.strip() == None:
            plannedAvailableDateTimeidentifi7 = 'tidak ada'
        print "plannedAvailableDateTimeidentifi7:", plannedAvailableDateTimeidentifi7
    except:
        plannedAvailableDateTimeidentifi7 = 'Tidak Ada'
        print "Passed27 plannedAvailableDateTimeidentifi7"

    try:   
        orderingInstructionsidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributionOrderProcess']['gmd:MD_StandardOrderProcess']['gmd:orderingInstructions']['gco:CharacterString']
        if orderingInstructionsidentifi7.strip() == None:
            orderingInstructionsidentifi7 = 'tidak ada'
        print "orderingInstructionsidentifi7:", orderingInstructionsidentifi7
    except:
        orderingInstructionsidentifi7 = 'Tidak Ada'
        print "Passed27 orderingInstructionsidentifi7"

    try:   
        turnaroundidentifi7 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributionOrderProcess']['gmd:MD_StandardOrderProcess']['gmd:turnaround']['gco:CharacterString']
        if turnaroundidentifi7.strip() == None:
            turnaroundidentifi7 = 'tidak ada'
        print "turnaroundidentifi7:", turnaroundidentifi7
    except:
        turnaroundidentifi7 = 'Tidak Ada'
        print "Passed27 turnaroundidentifi7"

    try:   
        nameidentifi8 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorFormat']['gmd:MD_Format']['gmd:name']['gco:CharacterString']
        if nameidentifi8.strip() == None:
            nameidentifi8 = 'tidak ada'
        print "nameidentifi8:", nameidentifi8
    except:
        nameidentifi8 = 'Tidak Ada'
        print "Passed27 nameidentifi8"

    try:   
        versionidentifi8 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorFormat']['gmd:MD_Format']['gmd:version']['gco:CharacterString']
        if versionidentifi8.strip() == None:
            versionidentifi8 = 'tidak ada'
        print "versionidentifi8:", versionidentifi8
    except:
        versionidentifi8 = 'Tidak Ada'
        print "Passed27 versionidentifi8"

    try:   
        amendmentNumberidentifi8 = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorFormat']['gmd:MD_Format']['gmd:amendmentNumber']['gco:CharacterString']
        if amendmentNumberidentifi8.strip() == None:
            amendmentNumberidentifi8 = 'tidak ada'
        print "amendmentNumberidentifi8:", amendmentNumberidentifi8
    except:
        amendmentNumberidentifi8 = 'Tidak Ada'
        print "Passed27 amendmentNumberidentifi8"

    try:   
        specificationidentifi8= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorFormat']['gmd:MD_Format']['gmd:specification']['gco:CharacterString']
        if specificationidentifi8.strip() == None:
            specificationidentifi8= 'tidak ada'
        print "specificationidentifi8:", specificationidentifi8
    except:
        specificationidentifi8= 'Tidak Ada'
        print "Passed27 specificationidentifi8"

    try:   
        fileDecompressionTechniqueidentifi8= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorFormat']['gmd:MD_Format']['gmd:fileDecompressionTechnique']['gco:CharacterString']
        if fileDecompressionTechniqueidentifi8.strip() == None:
            fileDecompressionTechniqueidentifi8= 'tidak ada'
        print "fileDecompressionTechniqueidentifi8:", fileDecompressionTechniqueidentifi8
    except:
        fileDecompressionTechniqueidentifi8= 'Tidak Ada'
        print "Passed27 fileDecompressionTechniqueidentifi8"


    try:   
        unitsOfDistribution= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:unitsOfDistribution']['gco:CharacterString']
        if unitsOfDistribution.strip() == None:
            unitsOfDistribution= 'tidak ada'
        print "unitsOfDistribution:", unitsOfDistribution
    except:
        unitsOfDistribution= 'Tidak Ada'
        print "Passed27 unitsOfDistribution"

    try:   
        transferSize= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:transferSize']['gco:Real']
        if transferSize.strip() == None:
            transferSize= 'tidak ada'
        print "transferSize:", transferSize
    except:
        transferSize= 'Tidak Ada'
        print "Passed27 transferSize"

    try:   
        linkageidentify9= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource']['gmd:linkage']['gmd:URL']
        if linkageidentify9.strip() == None:
            linkageidentify9= 'tidak ada'
        print "linkageidentify9:", linkageidentify9
    except:
        linkageidentify9= 'Tidak Ada'
        print "Passed27 linkageidentify9"

    try:   
        protocolidentify9= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource']['gmd:protocol']['gco:CharacterString']
        if protocolidentify9.strip() == None:
            protocolidentify9= 'tidak ada'
        print "protocolidentify9:", protocolidentify9
    except:
        protocolidentify9= 'Tidak Ada'
        print "Passed27 protocolidentify9"

    try:   
        applicationProfileidentify9= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource']['gmd:applicationProfile']['gco:CharacterString']
        if applicationProfileidentify9.strip() == None:
            applicationProfileidentify9= 'tidak ada'
        print "applicationProfileidentify9:", applicationProfileidentify9
    except:
        applicationProfileidentify9= 'Tidak Ada'
        print "Passed27 applicationProfileidentify9"

    try:   
        nameidentify9= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource']['gmd:name']['gco:CharacterString']
        if nameidentify9.strip() == None:
            nameidentify9= 'tidak ada'
        print "nameidentify9:", nameidentify9
    except:
        nameidentify9= 'Tidak Ada'
        print "Passed27 nameidentify9"
        
    try:   
        descriptionidentify9= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource']['gmd:description']['gco:CharacterString']
        if descriptionidentify9.strip() == None:
            descriptionidentify9= 'tidak ada'
        print "descriptionidentify9:", descriptionidentify9
    except:
        descriptionidentify9= 'Tidak Ada'
        print "Passed27 descriptionidentify9"

    try:   
        functionidentify9= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource']['gmd:function']['gmd:CI_OnLineFunctionCode']
        if functionidentify9.strip() == None:
            functionidentify9= 'tidak ada'
        print "functionidentify9:", functionidentify9
    except:
        functionidentify9= 'Tidak Ada'
        print "Passed27 functionidentify9"

    try:   
        nameMediumCode= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:offLine']['gmd:MD_Medium']['gmd:name']['gmd:MD_MediumNameCode']
        if nameMediumCode.strip() == None:
            nameMediumCode= 'tidak ada'
        print "nameMediumCode:", nameMediumCode
    except:
        nameMediumCode= 'Tidak Ada'
        print "Passed27 nameMediumCode"

    try:   
        density= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:offLine']['gmd:MD_Medium']['gmd:density']['gco:Real']
        if density.strip() == None:
            density= 'tidak ada'
        print "density:", density
    except:
        density= 'Tidak Ada'
        print "Passed27 density"

    try:   
        densityUnits= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:offLine']['gmd:MD_Medium']['gmd:densityUnits']['gco:CharacterString']
        if densityUnits.strip() == None:
            densityUnits= 'tidak ada'
        print "densityUnits:", densityUnits
    except:
        densityUnits= 'Tidak Ada'
        print "Passed27 densityUnits"

    try:   
        volumes= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:offLine']['gmd:MD_Medium']['gmd:volumes']['gco:Integer']
        if volumes.strip() == None:
            volumes= 'tidak ada'
        print "volumes:", volumes
    except:
        volumes= 'Tidak Ada'
        print "Passed27 volumes"

    try:   
        mediumFormat= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:offLine']['gmd:MD_Medium']['gmd:mediumFormat']['gmd:MD_MediumFormatCode']
        if mediumFormat.strip() == None:
            mediumFormat= 'tidak ada'
        print "mediumFormat:", mediumFormat
    except:
        mediumFormat= 'Tidak Ada'
        print "Passed27 mediumFormat"

    try:   
        mediumNote= dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceFormat']['gmd:MD_Format']['gmd:formatDistributor']['gmd:MD_Distributor']['gmd:distributorTransferOptions']['gmd:MD_DigitalTransferOptions']['gmd:offLine']['gmd:MD_Medium']['gmd:mediumNote']['gco:CharacterString']
        if mediumNote.strip() == None:
            mediumNote= 'tidak ada'
        print "mediumNote:", mediumNote
    except:
        mediumNote= 'Tidak Ada'
        print "Passed27 mediumNote"

    try:   
        specificUsage = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceSpecificUsage']['gmd:MD_Usage']['gmd:specificUsage']['gco:CharacterString']
        if specificUsage.strip() == None:
            specificUsage = 'tidak ada'
        print "specificUsage:", specificUsage
    except:
        specificUsage = 'Tidak Ada'
        print "Passed27 specificUsage"

    try:   
        useLimitation = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:resourceConstraints']['gmd:MD_Constraints']['gmd:useLimitation']['gco:CharacterString']
        if useLimitation.strip() == None:
            useLimitation = 'tidak ada'
        print "useLimitation:", useLimitation
    except:
        useLimitation = 'Tidak Ada'
        print "Passed27 useLimitation"

    try:   
        associationType = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:aggregationInfo']['gmd:MD_AggregateInformation']['gmd:associationType']['gmd:DS_AssociationTypeCode']
        if associationType.strip() == None:
            associationType = 'tidak ada'
        print "associationType:", associationType
    except:
        associationType = 'Tidak Ada'
        print "Passed27 associationType"

    try:   
        initiativeType = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:aggregationInfo']['gmd:MD_AggregateInformation']['gmd:initiativeType']['gmd:DS_InitiativeTypeCode']
        if initiativeType.strip() == None:
            initiativeType = 'tidak ada'
        print "initiativeType:", initiativeType
    except:
        initiativeType = 'Tidak Ada'
        print "Passed27 initiativeType"    

    try:   
        spatialRepresentationType = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:spatialRepresentationType']['gmd:MD_SpatialRepresentationTypeCode']
        if spatialRepresentationType.strip() == None:
            spatialRepresentationType = 'tidak ada'
        print "spatialRepresentationType:", spatialRepresentationType
    except:
        spatialRepresentationType = 'Tidak Ada'
        print "Passed27 spatialRepresentationType"

    try:   
        denominator = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:spatialResolution'][0]['gmd:MD_Resolution']['gmd:equivalentScale']['gmd:MD_RepresentativeFraction']['gmd:denominator']['gco:Integer']
        if denominator.strip() == None:
            denominator = 'tidak ada'
        print "denominator:", denominator
    except:
        denominator = 'Tidak Ada'
        print "Passed27 denominator"

    try:   
        distance = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:spatialResolution'][1]['gmd:MD_Resolution']['gmd:distance']['gco:Distance']
        if distance.strip() == None:
            distance = 'tidak ada'
        print "distance:", distance
    except:
        distance = 'Tidak Ada'
        print "Passed27 distance"


    try:   
        languageIdentify = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:language']['gco:CharacterString']
        if languageIdentify.strip() == None:
            languageIdentify = 'tidak ada'
        print "languageIdentify:", languageIdentify
    except:
        languageIdentify = 'Tidak Ada'
        print "Passed27 languageIdentify"



    try:   
        characterSet = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:characterSet']['gmd:MD_CharacterSetCode']
        if characterSet.strip() == None:
            characterSet = 'tidak ada'
        print "characterSet:", characterSet
    except:
        characterSet = 'Tidak Ada'
        print "Passed31 characterSet" 

    try:   
        topicCategory = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:topicCategory']['gmd:MD_TopicCategoryCode']
        if topicCategory.strip() == None:
            topicCategory = 'tidak ada'
        print "topicCategory:", topicCategory
    except:
        topicCategory = 'Tidak Ada'
        print "Passed31 topicCategory" 


    try:   
        environmentDescription = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:environmentDescription']['gco:CharacterString']
        if environmentDescription.strip() == None:
            environmentDescription = 'tidak ada'
        print "environmentDescription:", environmentDescription
    except:
        environmentDescription = 'Tidak Ada'
        print "Passed31 environmentDescription" 


    try:   
        westBoundLongitude = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:extent']['gmd:EX_Extent']['gmd:geographicElement']['gmd:EX_GeographicBoundingBox']['gmd:westBoundLongitude']['gco:Decimal']
        if westBoundLongitude.strip() == None:
            westBoundLongitude = 'tidak ada'
        print "westBoundLongitude:", westBoundLongitude
    except:
      westBoundLongitude = 'Tidak Ada'
      print "Passed28 westBoundLongitude"
    try:   
        eastBoundLongitude = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:extent']['gmd:EX_Extent']['gmd:geographicElement']['gmd:EX_GeographicBoundingBox']['gmd:eastBoundLongitude']['gco:Decimal']
        if eastBoundLongitude.strip() == None:
            eastBoundLongitude = 'tidak ada'
        print "eastBoundLongitude:", eastBoundLongitude
    except:
      eastBoundLongitude = 'Tidak Ada'
      print "Passed29 eastBoundLongitude"	
    try:   
        southBoundLatitude = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:extent']['gmd:EX_Extent']['gmd:geographicElement']['gmd:EX_GeographicBoundingBox']['gmd:southBoundLatitude']['gco:Decimal']
        if southBoundLatitude.strip() == None:
            southBoundLatitude = 'tidak ada'
        print "southBoundLatitude:", southBoundLatitude
    except:
      southBoundLatitude = 'Tidak Ada'
      print "Passed30 southBoundLatitude"	
    try:   
        northBoundLatitude = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:extent']['gmd:EX_Extent']['gmd:geographicElement']['gmd:EX_GeographicBoundingBox']['gmd:northBoundLatitude']['gco:Decimal']
        if northBoundLatitude.strip() == None:
            northBoundLatitude = 'tidak ada'
        print "northBoundLatitude:", northBoundLatitude
    except:
      northBoundLatitude = 'Tidak Ada'
      print "Passed31 northBoundLatitude"	
    try:   
        supplementalInformation = dictxml['gmd:MD_Metadata']['gmd:identificationInfo']['gmd:MD_DataIdentification']['gmd:supplementalInformation']['gco:CharacterString']
        if supplementalInformation.strip() == None:
            supplementalInformation = 'tidak ada'
        print "supplementalInformation:", supplementalInformation
    except:
        supplementalInformation = 'Tidak Ada'
        print "Passed31 supplementalInformation" 
    #===========================================================================================================================================================================================================

    #===================================================================  contentnInfo  ===========================================================================================================

    #===========================================================================================================================================================================================================

    print "                       "
    print "======================="
    print "  contentInfo               "
    print "======================="


    try:   
        complianceCode = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][0]['gmd:MD_FeatureCatalogueDescription']['gmd:complianceCode']['gco:Boolean']
        if complianceCode.strip() == None:
            complianceCode = 'tidak ada'
        print "complianceCode:", complianceCode
    except:
      complianceCode = 'Tidak Ada'
      print "Passed32 complianceCode"
    try:   
        languageConten = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][0]['gmd:MD_FeatureCatalogueDescription']['gmd:language']['gco:Boolean']
        if languageConten.strip() == None:
            languageConten = 'tidak ada'
        print "languageConten:", languageConten
    except:
        languageConten = 'Tidak Ada'
        print "Passed32 languageConten"
    try:   
        includedWithDataset = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][0]['gmd:MD_FeatureCatalogueDescription']['gmd:featureTypes']['gco:Boolean']
        if includedWithDataset.strip() == None:
            includedWithDataset = 'tidak ada'
        print "includedWithDataset:", includedWithDataset
    except:
      includedWithDataset = 'Tidak Ada'
      print "Passed33 includedWithDataset"
    try:   
        featureTypes = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][0]['gmd:MD_FeatureCatalogueDescription']['gmd:featureTypes']
        if featureTypes.strip() == None:
            featureTypes = 'tidak ada'
        print "featureTypes:", featureTypes
    except:
        featureTypes = 'Tidak Ada'
        print "Passed331 featureTypes"

    try:   
        featureCatalogueCitation = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][0]['gmd:MD_FeatureCatalogueDescription']['gmd:featureCatalogueCitation']
        if featureCatalogueCitation.strip() == None:
            featureCatalogueCitation = 'tidak ada'
        print "featureCatalogueCitation:", featureCatalogueCitation
    except:
        featureCatalogueCitation = 'Tidak Ada'
        print "Passed331 featureCatalogueCitation"

    try:   
        attributeDescription = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:attributeDescription']
        if attributeDescription.strip() == None:
            attributeDescription = 'tidak ada'
        print "attributeDescription:", attributeDescription
    except:
        attributeDescription = 'Tidak Ada'
        print "Passed332 attributeDescription"
    try:   
        contentType = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:contentType']
        if contentType.strip() == None:
            contentType = 'tidak ada'
        print "contentType:", contentType
    except:
        contentType = 'Tidak Ada'
        print "Passed333 contentType"

    try:   
        dimension = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:dimension']
        if dimension.strip() == None:
            dimension = 'tidak ada'
        print "dimension:", dimension
    except:
        dimension = 'Tidak Ada'
        print "Passed334 dimension"    

    try:   
        illuminationElevationAngle = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:illuminationElevationAngle']['gco:Real']
        if illuminationElevationAngle.strip() == None:
            illuminationElevationAngle = 'tidak ada'
        print "illuminationElevationAngle:", illuminationElevationAngle
    except:
        illuminationElevationAngle = 'Tidak Ada'
        print "Passed335 illuminationElevationAngle"

    try:   
        illuminationAzimuthAngle = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:illuminationAzimuthAngle']['gco:Real']
        if illuminationAzimuthAngle.strip() == None:
            illuminationAzimuthAngle = 'tidak ada'
        print "illuminationAzimuthAngle:", illuminationAzimuthAngle
    except:
        illuminationAzimuthAngle = 'Tidak Ada'
        print "Passed336 illuminationAzimuthAngle"


    try:   
        imagingCondition = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:imagingCondition']
        if imagingCondition.strip() == None:
            imagingCondition = 'tidak ada'
        print "imagingCondition:", imagingCondition
    except:
        imagingCondition = 'Tidak Ada'
        print "Passed338 imagingCondition"

    try:   
        imageQualityCode = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:imageQualityCode']
        if imageQualityCode.strip() == None:
            imageQualityCode = 'tidak ada'
        print "imageQualityCode:", imageQualityCode
    except:
        imageQualityCode = 'Tidak Ada'
        print "Passed339 imageQualityCode"    

    try:   
        cloudCoverPercentage = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:cloudCoverPercentage']['gco:Real']
        if cloudCoverPercentage.strip() == None:
            cloudCoverPercentage = 'tidak ada'
        print "cloudCoverPercentage:", cloudCoverPercentage
    except:
        cloudCoverPercentage = 'Tidak Ada'
        print "Passed3391 cloudCoverPercentage"

    try:   
        processingLevelCode = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:processingLevelCode']
        if processingLevelCode.strip() == None:
            processingLevelCode = 'tidak ada'
        print "processingLevelCode:", processingLevelCode
    except:
        processingLevelCode = 'Tidak Ada'
        print "Passed33911 processingLevelCode"

    try:   
        compressionGenerationQuantity = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:compressionGenerationQuantity']
        if compressionGenerationQuantity.strip() == None:
            compressionGenerationQuantity = 'tidak ada'
        print "compressionGenerationQuantity:", compressionGenerationQuantity
    except:
        compressionGenerationQuantity = 'Tidak Ada'
        print "Passed33912 compressionGenerationQuantity"

    try:   
        triangulationIndicator = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:triangulationIndicator']['gco:Boolean']
        if triangulationIndicator.strip() == None:
            triangulationIndicator = 'tidak ada'
        print "triangulationIndicator:", triangulationIndicator
    except:
        triangulationIndicator = 'Tidak Ada'
        print "Passed33913 triangulationIndicator"    

    try:   
        radiometricCalibrationDataAvailability = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:radiometricCalibrationDataAvailability']['gco:Boolean']
        if radiometricCalibrationDataAvailability.strip() == None:
            radiometricCalibrationDataAvailability = 'tidak ada'
        print "radiometricCalibrationDataAvailability:", radiometricCalibrationDataAvailability
    except:
        radiometricCalibrationDataAvailability = 'Tidak Ada'
        print "Passed33914 radiometricCalibrationDataAvailability"

    try:   
        cameraCalibrationInformationAvailability = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:cameraCalibrationInformationAvailability']['gco:Boolean']
        if cameraCalibrationInformationAvailability.strip() == None:
            cameraCalibrationInformationAvailability = 'tidak ada'
        print "cameraCalibrationInformationAvailability:", cameraCalibrationInformationAvailability
    except:
        cameraCalibrationInformationAvailability = 'Tidak Ada'
        print "Passed33915 cameraCalibrationInformationAvailability"

    try:   
        filmDistortionInformationAvailability = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:filmDistortionInformationAvailability']['gco:Boolean']
        if filmDistortionInformationAvailability.strip() == None:
            filmDistortionInformationAvailability = 'tidak ada'
        print "filmDistortionInformationAvailability:", filmDistortionInformationAvailability
    except:
        filmDistortionInformationAvailability = 'Tidak Ada'
        print "Passed33916 filmDistortionInformationAvailability"

    try:   
        lensDistortionInformationAvailability = dictxml['gmd:MD_Metadata']['gmd:contentInfo'][1]['gmd:MD_CoverageDescription']['gmd:lensDistortionInformationAvailability']['gco:Boolean']
        if lensDistortionInformationAvailability.strip() == None:
            lensDistortionInformationAvailability = 'tidak ada'
        print "lensDistortionInformationAvailability:", lensDistortionInformationAvailability
    except:
        lensDistortionInformationAvailability = 'Tidak Ada'
        print "Passed33917 lensDistortionInformationAvailability"


    #===========================================================================================================================================================================================================

    #===================================================================  distributionInfo  ===========================================================================================================

    #===========================================================================================================================================================================================================

    print "                       "
    print "======================="
    print "  distributionInfo              "
    print "======================="

    try:   
        namedistribusi = dictxml['gmd:MD_Metadata']['gmd:distributionInfo']['gmd:MD_Distribution']['gmd:distributionFormat']['gmd:MD_Format']['gmd:name']['gco:CharacterString']
        if namedistribusi.strip() == None:
            namedistribusi = 'tidak ada'
        print "namedistribusi':", namedistribusi
    except:
      namedistribusi = 'Tidak Ada'
      print "Passed34 namedistribusi"
    try:   
        versiondistribusi = dictxml['gmd:MD_Metadata']['gmd:distributionInfo']['gmd:MD_Distribution']['gmd:distributionFormat']['gmd:MD_Format']['gmd:version']['gco:CharacterString']
        if versiondistribusi.strip() == None:
            versiondistribusi = 'tidak ada'
        print "versiondistribusi':", versiondistribusi
    except:
        versiondistribusi = 'Tidak Ada'
        print "Passed35 versiondistribusi"

    try:   
        linkagedistribusiol = dictxml['gmd:MD_Metadata']['gmd:distributionInfo']['gmd:MD_Distribution']['gmd:transferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource'] ['gmd:linkage']['gmd:URL']
        if linkagedistribusiol.strip() == None:
            linkagedistribusiol = 'tidak ada'
        print "linkagedistribusiol:", linkagedistribusiol
    except:
      linkagedistribusiol = 'Tidak Ada'
      print "Passed351 linkagedistribusiol"
    try:   
        namedistribusiol = dictxml['gmd:MD_Metadata']['gmd:distributionInfo']['gmd:MD_Distribution']['gmd:transferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource'] ['gmd:name']['gco:CharacterString']
        if namedistribusiol.strip() == None:
            namedistribusiol = 'tidak ada'
        print "namedistribusiol:", namedistribusiol
    except:
      namedistribusiol = 'Tidak Ada'
      print "Passed36 namedistribusiol"
    try:   
        descriptiondistribusiol = dictxml['gmd:MD_Metadata']['gmd:distributionInfo']['gmd:MD_Distribution']['gmd:transferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource'] ['gmd:description']['gco:CharacterString']
        if descriptiondistribusiol.strip() == None:
            descriptiondistribusiol = 'tidak ada'
        print "descriptiondistribusiol:", descriptiondistribusiol
    except:
      descriptiondistribusiol = 'Tidak Ada'
      print "Passed37 descriptiondistribusiol"
    try:   
        functiondistribusiol = dictxml['gmd:MD_Metadata']['gmd:distributionInfo']['gmd:MD_Distribution']['gmd:transferOptions']['gmd:MD_DigitalTransferOptions']['gmd:onLine']['gmd:CI_OnlineResource'] ['gmd:function']['gmd:CI_OnLineFunctionCode']
        if functiondistribusiol.strip() == None:
            functiondistribusiol = 'tidak ada'
        print "functiondistribusiol:", functiondistribusiol
    except:
      functiondistribusiol = 'Tidak Ada'
      print "Passed38 functiondistribusiol"	

    #==================================================================================================================================================================================================

    #===================================================================  portrayalCatalogueInfo  =====================================================================================================

    #===================================================================================================================================================================================================

    print "                       "
    print "======================="
    print "  portrayalCatalogueInfo            "
    print "======================="



    try:   
        titlepot = dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:title']['gco:CharacterString']
        if titlepot.strip() == None:
            titlepot = 'tidak ada'
        print "titlepot:", titlepot
    except:
      titlepot = 'Tidak Ada titles'
      print "Passed39 titlepot"

    try:   
        datepot = dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:date']['gmd:CI_Date']['gmd:date']['gco:DateTime']
        if datepot.strip() == None:
            datepot = 'tidak ada'
        print "datepot:", datepot
    except:
        datepot = 'Tidak Ada titles'
        print "Passed39 datepot"

    try:   
        editionpot = dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:edition']['gco:CharacterString']
        if editionpot.strip() == None:
            editionpot = 'tidak ada'
        print "editionpot:", editionpot
    except:
        editionpot = 'Tidak Ada titles'
        print "Passed39 editionpot"

    try:   
        individualNamepot = dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:individualName']['gco:CharacterString']
        if individualNamepot.strip() == None:
            individualNamepot = 'tidak ada'
        print "individualNamepot:", individualNamepot
    except:
        individualNamepot = 'Tidak Ada titles'
        print "Passed39 individualNamepot"

    try:   
        organisationNamepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:organisationName']['gco:CharacterString']
        if organisationNamepot.strip() == None:
            organisationNamepot= 'tidak ada'
        print "organisationNamepot:", organisationNamepot
    except:
        organisationNamepot= 'Tidak Ada titles'
        print "Passed39 organisationNamepot"

    try:  
        positionNamepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:positionName']['gco:CharacterString']
        if positionNamepot.strip() == None:
            positionNamepot= 'tidak ada'
        print "positionNamepot:", positionNamepot
    except:
        positionNamepot= 'Tidak Ada titles'
        print "Passed39 positionNamepot"

    try:  
        voicepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:voice']['gco:CharacterString']
        if voicepot.strip() == None:
            voicepot= 'tidak ada'
        print "voicepot:", voicepot
    except:
        voicepot= 'Tidak Ada titles'
        print "Passed39 voicepot"
    try:  
        facsmilepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:phone']['gmd:CI_Telephone']['gmd:facsmile']['gco:CharacterString']
        if facsmilepot.strip() == None:
            facsmilepot= 'tidak ada'
        print "facsmilepot:", facsmilepot
    except:
        facsmilepot= 'Tidak Ada titles'
        print "Passed39 facsmilepot"

    try:  
        deliveryPointpot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:deliveryPoint']['gco:CharacterString']
        if deliveryPointpot.strip() == None:
            deliveryPointpot= 'tidak ada'
        print "deliveryPointpot:", deliveryPointpot
    except:
        deliveryPointpot= 'Tidak Ada titles'
        print "Passed39 deliveryPointpot"

    try:  
        citypot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:city']['gco:CharacterString']
        if citypot.strip() == None:
            citypot= 'tidak ada'
        print "citypot:", citypot
    except:
        citypot= 'Tidak Ada titles'
        print "Passed39 citypot"

    try:  
        administrativeAreapot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:administrativeArea']['gco:CharacterString']
        if administrativeAreapot.strip() == None:
            administrativeAreapot= 'tidak ada'
        print "administrativeAreapot:", administrativeAreapot
    except:
        administrativeAreapot= 'Tidak Ada titles'
        print "Passed39 administrativeAreapot" 

    try:  
        postalCodepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:postalCode']['gco:CharacterString']
        if postalCodepot.strip() == None:
            postalCodepot= 'tidak ada'
        print "postalCodepot:", postalCodepot
    except:
        postalCodepot= 'Tidak Ada titles'
        print "Passed39 postalCodepot"    

    try:  
        countrypot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:country']['gco:CharacterString']
        if countrypot.strip() == None:
            countrypot= 'tidak ada'
        print "countrypot:", countrypot
    except:
        countrypot= 'Tidak Ada titles'
        print "Passed39 countrypot"    

    try:  
        electronicMailAddresspot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:address']['gmd:CI_Address']['gmd:electronicMailAddress']['gco:CharacterString']
        if electronicMailAddresspot.strip() == None:
            electronicMailAddresspot= 'tidak ada'
        print "electronicMailAddresspot:", electronicMailAddresspot
    except:
        electronicMailAddresspot= 'Tidak Ada titles'
        print "Passed39 electronicMailAddresspot"


    try:  
        linkagepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:linkage']['gmd:URL']
        if linkagepot.strip() == None:
            linkagepot= 'tidak ada'
        print "linkagepot:", linkagepot
    except:
        linkagepot= 'Tidak Ada titles'
        print "Passed39 linkagepot"

    try:  
        namepot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:name']['gco:CharacterString']
        if namepot.strip() == None:
            namepot= 'tidak ada'
        print "namepot:", namepot
    except:
        namepot= 'Tidak Ada titles'
        print "Passed39 namepot"


    try:  
        descriptionpot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:description']['gco:CharacterString']
        if descriptionpot.strip() == None:
            descriptionpot= 'tidak ada'
        print "descriptionpot:", descriptionpot
    except:
        descriptionpot= 'Tidak Ada titles'
        print "Passed39 descriptionpot"


    try:  
        functionpot= dictxml['gmd:MD_Metadata']['gmd:portrayalCatalogueInfo']['gmd:MD_PortrayalCatalogueReference']['gmd:portrayalCatalogueCitation']['gmd:CI_Citation']['gmd:citedResponsibleParty']['gmd:CI_ResponsibleParty']['gmd:contactInfo']['gmd:CI_Contact']['gmd:onlineResource']['gmd:CI_OnlineResource']['gmd:function']['gmd:CI_OnLineFunctionCode']
        if functionpot.strip() == None:
            functionpot= 'tidak ada'
        print "functionpot:", functionpot
    except:
        functionpot= 'Tidak Ada titles'
        print "Passed39 functionpot"

    #=====================================================================================================================================================================================================

    #===================================================================  metadataConstraints  ===========================================================================================================

    #======================================================================================================================================================================================================

    print "                       "
    print "======================="
    print "  metadataConstraints               "
    print "======================="

    try:   
        useLimitation = dictxml['gmd:MD_Metadata']['gmd:metadataConstraints']['gmd:MD_Constraints']['gmd:useLimitation']['gco:CharacterString']
        if useLimitation.strip() == None:
            useLimitation = 'tidak ada'
        print "useLimitation:", useLimitation
    except:
      useLimitation = 'Tidak Ada'
      print "Passed40 useLimitation"



    #=====================================================================================================================================================================================================

    #===================================================================  metadataMaintenance  ===========================================================================================================

    #=====================================================================================================================================================================================================
    print "                       "
    print "======================="
    print "  metadataMaintenance               "
    print "======================="



    try:   
        maintenanceAndUpdateFrequency = dictxml['gmd:MD_Metadata']['gmd:metadataMaintenance']['gmd:MD_MaintenanceInformation']['gmd:maintenanceAndUpdateFrequency']['gmd:MD_MaintenanceFrequencyCode']
        if maintenanceAndUpdateFrequency.strip() == None:
            maintenanceAndUpdateFrequency = 'tidak ada'
        print "maintenanceAndUpdateFrequency:", maintenanceAndUpdateFrequency
    except:
      maintenanceAndUpdateFrequency = 'Tidak Ada'
      print "Passed41 maintenanceAndUpdateFrequency"
    try:   
        updateScope = dictxml['gmd:MD_Metadata']['gmd:metadataMaintenance']['gmd:MD_MaintenanceInformation']['gmd:updateScope']['gmd:MD_ScopeCode']
        if updateScope.strip() == None:
            updateScope = 'tidak ada'
        print "updateScope:", updateScope
    except:
        updateScope = 'Tidak Ada'
        print "Passed42 updateScope"
    try:   
        updateScopeDescription = dictxml['gmd:MD_Metadata']['gmd:metadataMaintenance']['gmd:MD_MaintenanceInformation']['gmd:updateScopeDescription']['gmd:MD_ScopeDescription']
        if updateScopeDescription.strip() == None:
            updateScopeDescription = 'tidak ada'
        print "updateScopeDescription:", updateScopeDescription
    except:
        updateScopeDescription = 'Tidak Ada'
        print "Passed43 updateScopeDescription"
    try:   
        maintenanceNote = dictxml['gmd:MD_Metadata']['gmd:metadataMaintenance']['gmd:MD_MaintenanceInformation']['gmd:maintenanceNote']['gco:CharacterString']
        if maintenanceNote.strip() == None:
            maintenanceNote = 'tidak ada'
        print "maintenanceNote:", maintenanceNote
    except:
        maintenanceNote = 'Tidak Ada'
        print "Passed44 maintenanceNote"




    #=============================================================================================================================================================================================

    #===================================================================  Parsing File  ===========================================================================================================

    #==============================================================================================================================================================================================







    # print(urllib2.unquote(xml_payload))
    with open(cfg.APP_BASE + 'CP-indonesia.mcf', 'r') as file_xml_template:
        xml_template = file_xml_template.read()

    #try:         
        
        #================================== Md_Metadata ========================================
        
        #=======================================================================================
    # xml_template = xml_template.replace('$$rep:fileIdentifier$$', fileIdentifier) #1
    # xml_template = xml_template.replace('$$rep:language$$', language) #2
    xml_template = xml_template.replace('$$rep:hierarchyLevel$$',  hierarchyLevel) #3
    xml_template = xml_template.replace('$$rep:hierarchyLevelName$$',  hierarchyLevelName) #4

        #================================== Contact ============================================
        
        #=======================================================================================
    xml_template = xml_template.replace('$$rep:individualName$$',  individualName) #5
    print 'TEST:', organisationName
    xml_template = xml_template.replace('$$rep:organisationName$$',  organisationName) #6
    xml_template = xml_template.replace('$$rep:positionName$$',  positionName) #6
    xml_template = xml_template.replace('$$rep:voice$$',  voice) #7
    xml_template = xml_template.replace('$$rep:facsimile$$',  facsimile) #8
    xml_template = xml_template.replace('$$rep:deliveryPoint$$',  deliveryPoint) #9
    xml_template = xml_template.replace('$$rep:city$$',  city) #10
    xml_template = xml_template.replace('$$rep:administrativeArea$$',  administrativeArea) #11
    xml_template = xml_template.replace('$$rep:postalCode$$',  postalCode) #12
    xml_template = xml_template.replace('$$rep:country$$',  country) #13
    xml_template = xml_template.replace('$$rep:electronicMailAddress$$',  electronicMailAddress) #14
    xml_template = xml_template.replace('$$rep:linkagecontact$$',  linkagecontact)
    xml_template = xml_template.replace('$$rep:namecontact$$', namecontact)
    xml_template = xml_template.replace('$$rep:descriptioncontact$$', descriptioncontact)
    xml_template = xml_template.replace('$$rep:functioncontact$$', functioncontact )
    xml_template = xml_template.replace('$$rep:CI_RoleCode$$',  CI_RoleCode) #15
    xml_template = xml_template.replace('$$rep:dateStamp$$',  dateStamp) #16
    xml_template = xml_template.replace('$$rep:metadataStandardName$$',  metadataStandardName) #161
    xml_template = xml_template.replace('$$rep:metadataStandardVersion$$',  metadataStandardVersion) #162
    xml_template = xml_template.replace('$$rep:dataSetURI$$',  dataSetURI) #163

        #===================================================================  spatialRepresentationInfo  ===========================================================

        #===========================================================================================================================================================

    xml_template = xml_template.replace('$$rep:dimensionName$$',  dimensionName) #17
    xml_template = xml_template.replace('$$rep:dimensionSize$$', dimensionSize) #18
    xml_template = xml_template.replace('$$rep:resolution$$',  resolution) #19
    xml_template = xml_template.replace('$$rep:topologyLevel$$', topologyLevel ) #19
    xml_template = xml_template.replace('$$rep:geometricObjectType$$', geometricObjectType) #19
    xml_template = xml_template.replace('$$rep:geometricObjectCount$$', geometricObjectCount) #19
    xml_template = xml_template.replace('$$rep:checkPointAvailability$$', checkPointAvailability ) #19
    xml_template = xml_template.replace('$$rep:checkPointDescription$$', checkPointDescription ) #19
    xml_template = xml_template.replace('$$rep:controlPointAvailability$$', controlPointAvailability ) #19
    xml_template = xml_template.replace('$$rep:orientationParameterDescription$$', orientationParameterDescription ) #19
    xml_template = xml_template.replace('$$rep:titlegeoreferenceable$$', titlegeoreferenceable ) #19
    xml_template = xml_template.replace('$$rep:dategeoreferenceable$$', dategeoreferenceable) #19
    xml_template = xml_template.replace('$$rep:editiongeoreferenceable$$', editiongeoreferenceable) #19


    #===================================================================  referenceSystemInfo  ======================================================================

    #================================================================================================================================================================
        
    xml_template = xml_template.replace('$$rep:code$$', code) #20
    xml_template = xml_template.replace('$$rep:codeSpace$$',  codeSpace) #21
    xml_template = xml_template.replace('$$rep:version$$',  version) #22
    xml_template = xml_template.replace('$$rep:code1$$', code1) #20
    xml_template = xml_template.replace('$$rep:codeSpace1$$',  codeSpace1) #21
    xml_template = xml_template.replace('$$rep:version1$$',  version1) #22
    xml_template = xml_template.replace('$$rep:code2$$', code2) #20
    xml_template = xml_template.replace('$$rep:codeSpace2$$',  codeSpace2) #21
    xml_template = xml_template.replace('$$rep:version2$$',  version2) #22
    xml_template = xml_template.replace('$$rep:code3$$', code3) #20
    xml_template = xml_template.replace('$$rep:codeSpace3$$',  codeSpace3) #21
    xml_template = xml_template.replace('$$rep:version3$$',  version3) #22

    #===================================================================  identificationInfo  =====================================================================

    #==============================================================================================================================================================   

    xml_template = xml_template.replace('$$rep:title$$',  title) #23
    xml_template = xml_template.replace('$$rep:alternateTitle$$',  alternateTitle) #24
    xml_template = xml_template.replace('$$rep:date$$', date) #25
    xml_template = xml_template.replace('$$rep:edition$$',  edition) #26
    xml_template = xml_template.replace('$$rep:individualNameIdentifi$$', individualNameIdentifi ) #27
    xml_template = xml_template.replace('$$rep:organisationNameIdentifi$$', organisationNameIdentifi ) #27
    xml_template = xml_template.replace('$$rep:positioNameIdentifi$$', positionNameIdentifi) #27
    xml_template = xml_template.replace('$$rep:voiceIdentifi$$', voiceIdentifi) #27
    xml_template = xml_template.replace('$$rep:abstract$$', abstract) #27
    xml_template = xml_template.replace('$$rep:purpose$$', purpose) #27
    xml_template = xml_template.replace('$$rep:credit$$', credit) #27
    xml_template = xml_template.replace('$$rep:status$$', status) #27
    xml_template = xml_template.replace('$$rep:individualNameIdentifi2$$', individualNameidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:organisationNameidentifi2$$', organisationNameidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:positionNameidentifi2$$', positionNameidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:voiceidentifi2$$', voiceidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:facsimileidentifi2$$', facsimileidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:deliveryPointidentifi2$$', deliveryPointidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:cityidentifi2$$', cityidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:administrativeAreaidentifi2$$', administrativeAreaidentifi2) #27
    xml_template = xml_template.replace('$$rep:postalCodeidentifi2$$', postalCodeidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:countryidentifi2$$', countryidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:electronicMailAddressidentifi2$$', electronicMailAddressidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:linkageidentifi2$$', linkageidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:protocolidentifi2$$', protocolidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:applicationProfileidentifi2$$', applicationProfileidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:nameidentifi2$$', nameidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:descriptionidentifi2$$', descriptionidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:functionidentifi2$$', functionidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:hoursOfServiceidentifi2$$', hoursOfServiceidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:contactInstructionsidentifi2$$', contactInstructionsidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:CI_RoleCodeidentifi2$$', CI_RoleCodeidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:maintenanceAndUpdateFrequencyidentifi2$$', maintenanceAndUpdateFrequencyidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:dateOfNextUpdateidentifi2$$', dateOfNextUpdateidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:userDefinedMaintenanceFrequencyidentifi2$$', userDefinedMaintenanceFrequencyidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:updateScopeidentifi2$$', updateScopeidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:maintenanceNoteidentifi2$$', maintenanceNoteidentifi2 ) #27
    xml_template = xml_template.replace('$$rep:individualNameidentifi3$$', individualNameidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:organisationNameidentifi3$$', organisationNameidentifi3) #27
    xml_template = xml_template.replace('$$rep:positionNameNameidentifi3$$', positionNameNameidentifi3) #27
    xml_template = xml_template.replace('$$rep:voiceidentifi3$$', voiceidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:facsimileidentifi3$$', facsimileidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:descriptionidentifi3$$', descriptionidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:cityidentifi3$$', cityidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:administrativeAreaidentifi3$$', administrativeAreaidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:postalCodeidentifi3$$', postalCodeidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:countryidentifi3$$', countryidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:electronicMailAddressidentifi3$$', electronicMailAddressidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:linkageidentifi3$$', linkageidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:protocolidentifi3$$', protocolidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:applicationProfileidentifi3$$', applicationProfileidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:nameidentifi3$$', nameidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:descriptionidentifi3$$', descriptionidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:functionidentifi3$$', functionidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:hoursOfServiceidentifi3$$', hoursOfServiceidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:contactInstructionsidentifi3$$', contactInstructionsidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:roleidentifi3$$', roleidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:filenameidentifi3$$', filenameidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:fileDescriptionidentifi3$$', fileDescriptionidentifi3 ) #27
    xml_template = xml_template.replace('$$rep:fileTypeidentifi3$$', fileTypeidentifi3) #27
    xml_template = xml_template.replace('$$rep:amendmentNumber$$', amendmentNumber ) #27
    xml_template = xml_template.replace('$$rep:fileDecompressionTechnique$$', fileDecompressionTechnique) #27
    xml_template = xml_template.replace('$$rep:individualNameidentifi7$$', individualNameidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:organisationNameidentifi7$$', organisationNameidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:positionNameidentifi7$$', positionNameidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:voiceidentifi7$$', voiceidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:facsimileidentifi7$$', facsimileidentifi7) #27
    xml_template = xml_template.replace('$$rep:deliveryPointidentifi7$$', deliveryPointidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:cityidentifi7$$', cityidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:administrativeAreaidentifi7$$', administrativeAreaidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:postalCodeidentifi7$$', postalCodeidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:countryidentifi7$$', countryidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:electronicMailAddressidentifi7$$', electronicMailAddressidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:linkageidentifi7$$', linkageidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:protocolidentifi7$$', protocolidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:applicationProfileidentifi7$$', applicationProfileidentifi7) #27
    xml_template = xml_template.replace('$$rep:nameidentifi7$$', nameidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:descriptionidentifi7$$', descriptionidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:functionidentifi7$$', functionidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:hoursOfServiceidentifi7$$', hoursOfServiceidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:contactInstructionsidentifi7$$', contactInstructionsidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:roleidentifi7$$', roleidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:feesidentifi7$$', feesidentifi7) #27
    xml_template = xml_template.replace('$$rep:plannedAvailableDateTimeidentifi7$$', plannedAvailableDateTimeidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:orderingInstructionsidentifi7$$', orderingInstructionsidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:turnaroundidentifi7$$', turnaroundidentifi7 ) #27
    xml_template = xml_template.replace('$$rep:nameidentifi8$$', nameidentifi8) #27
    xml_template = xml_template.replace('$$rep:versionidentifi8$$', versionidentifi8 ) #27
    xml_template = xml_template.replace('$$rep:amendmentNumberidentifi8$$', amendmentNumberidentifi8 ) #27
    xml_template = xml_template.replace('$$rep:specificationidentifi8$$', specificationidentifi8 ) #27
    xml_template = xml_template.replace('$$rep:fileDecompressionTechniqueidentifi8$$', fileDecompressionTechniqueidentifi8 ) #27
    xml_template = xml_template.replace('$$rep:unitsOfDistribution$$', unitsOfDistribution ) #27
    xml_template = xml_template.replace('$$rep:transferSize$$', transferSize ) #27
    xml_template = xml_template.replace('$$rep:linkageidentify9$$', linkageidentify9) #27
    xml_template = xml_template.replace('$$rep:protocolidentify9$$', protocolidentify9 ) #27
    xml_template = xml_template.replace('$$rep:applicationProfileidentify9$$', applicationProfileidentify9 ) #27
    xml_template = xml_template.replace('$$rep:nameidentify9$$', nameidentify9 ) #27
    xml_template = xml_template.replace('$$rep:descriptionidentify9$$', descriptionidentify9 ) #27
    xml_template = xml_template.replace('$$rep:functionidentify9$$', functionidentify9) #27
    xml_template = xml_template.replace('$$rep:nameMediumCode$$', nameMediumCode ) #27
    xml_template = xml_template.replace('$$rep:density$$', density ) #27
    xml_template = xml_template.replace('$$rep:densityUnits$$', densityUnits ) #27
    xml_template = xml_template.replace('$$rep:volumes$$', volumes ) #27
    xml_template = xml_template.replace('$$rep:mediumFormat$$', mediumFormat ) #27
    xml_template = xml_template.replace('$$rep:mediumNote$$', mediumNote ) #27
    xml_template = xml_template.replace('$$rep:specificUsage$$', specificUsage ) #27
    xml_template = xml_template.replace('$$rep:useLimitation$$', useLimitation ) #27
    xml_template = xml_template.replace('$$rep:associationType$$', associationType ) #27
    xml_template = xml_template.replace('$$rep:initiativeType$$', initiativeType ) #27
    xml_template = xml_template.replace('$$rep:spatialRepresentationType$$', spatialRepresentationType ) #27
    xml_template = xml_template.replace('$$rep:denominator$$', denominator ) #27
    xml_template = xml_template.replace('$$rep:distance$$', distance) #27
    xml_template = xml_template.replace('$$rep:languageIdentify$$', languageIdentify) #27
    xml_template = xml_template.replace('$$rep:characterSet$$', characterSet ) #27
    xml_template = xml_template.replace('$$rep:topicCategory$$', topicCategory ) #27
    xml_template = xml_template.replace('$$rep:environmentDescription$$', environmentDescription ) #27
    xml_template = xml_template.replace('$$rep:wb84$$',  str(westBoundLongitude)) #28
    xml_template = xml_template.replace('$$rep:eb84$$',  str(eastBoundLongitude)) #29
    xml_template = xml_template.replace('$$rep:sb84$$',  str(southBoundLatitude)) #30
    xml_template = xml_template.replace('$$rep:nb84$$',  str(northBoundLatitude)) #31
    xml_template = xml_template.replace('$$rep:supplementalInformation$$', supplementalInformation) #27


    #===================================================================  contentnInfo  ===========================================================================

    #===============================================================================================================================================================

    xml_template = xml_template.replace('$$rep:complianceCode$$',  complianceCode) #32
    xml_template = xml_template.replace('$$rep:languageConten$$',  languageConten) #32
    xml_template = xml_template.replace('$$rep:includedWithDataset$$',  includedWithDataset) #33
    xml_template = xml_template.replace('$$rep:featureTypes$$', featureTypes) #32
    xml_template = xml_template.replace('$$rep:featureCatalogueCitation$$',  featureCatalogueCitation) #32
    xml_template = xml_template.replace('$$rep:attributeDescription$$', attributeDescription) #32
    xml_template = xml_template.replace('$$rep:contentType$$',  contentType) #32
    xml_template = xml_template.replace('$$rep:dimension$$', dimension) #32
    xml_template = xml_template.replace('$$rep:illuminationElevationAngle$$',  illuminationElevationAngle) #32
    xml_template = xml_template.replace('$$rep:illuminationAzimuthAngle$$', illuminationAzimuthAngle) #32
    xml_template = xml_template.replace('$$rep:imagingCondition$$', imagingCondition) #32
    xml_template = xml_template.replace('$$rep:imageQualityCode$$', imageQualityCode) #32
    xml_template = xml_template.replace('$$rep:cloudCoverPercentage$$',  cloudCoverPercentage) #32
    xml_template = xml_template.replace('$$rep:processingLevelCode$$',  processingLevelCode) #32
    xml_template = xml_template.replace('$$rep:compressionGenerationQuantity$$',  compressionGenerationQuantity) #32
    xml_template = xml_template.replace('$$rep:triangulationIndicator$$',  triangulationIndicator) #32
    xml_template = xml_template.replace('$$rep:radiometricCalibrationDataAvailability$$',  radiometricCalibrationDataAvailability) #32
    xml_template = xml_template.replace('$$rep:cameraCalibrationInformationAvailability$$',  cameraCalibrationInformationAvailability) #32
    xml_template = xml_template.replace('$$rep:filmDistortionInformationAvailability$$',  filmDistortionInformationAvailability) #32
    xml_template = xml_template.replace('$$rep:lensDistortionInformationAvailability$$',  lensDistortionInformationAvailability) #32



    #===================================================================  distributionInfo  ======================================================================

    #=============================================================================================================================================================



    xml_template = xml_template.replace('$$rep:namedistribusi$$',  namedistribusi) #34
    xml_template = xml_template.replace('$$rep:versiondistribusi$$',  versiondistribusi) #34
    xml_template = xml_template.replace('$$rep:linkagedistribusiol$$',  linkagedistribusiol) #351
    xml_template = xml_template.replace('$$rep:namedistribusiol$$',  namedistribusiol) #36
    xml_template = xml_template.replace('$$rep:descriptiondistribusiol$$',  descriptiondistribusiol) #37
    xml_template = xml_template.replace('$$rep:functiondistribusiol$$',  functiondistribusiol) #38


    #===================================================================  portrayalCatalogueInfo  =================================================================

    #==============================================================================================================================================================


    xml_template = xml_template.replace('$$rep:titlepot$$',  titlepot) #39
    xml_template = xml_template.replace('$$rep:datepot$$', datepot )
    xml_template = xml_template.replace('$$rep:editionpot$$', editionpot )
    xml_template = xml_template.replace('$$rep:individualNamepot$$', individualNamepot )
    xml_template = xml_template.replace('$$rep:organisationNamepot$$', organisationNamepot  )
    xml_template = xml_template.replace('$$rep:positionNamepot$$', positionNamepot )
    xml_template = xml_template.replace('$$rep:voicepot$$', voicepot )
    xml_template = xml_template.replace('$$rep:facsmilepot$$', facsmilepot )
    xml_template = xml_template.replace('$$rep:deliveryPointpot$$', deliveryPointpot  )
    xml_template = xml_template.replace('$$rep:citypot$$', citypot  )
    xml_template = xml_template.replace('$$rep:administrativeAreapot$$', administrativeAreapot  )
    xml_template = xml_template.replace('$$rep:postalCodepot$$', postalCodepot )
    xml_template = xml_template.replace('$$rep:countrypot$$', countrypot )
    xml_template = xml_template.replace('$$rep:electronicMailAddresspot$$', electronicMailAddresspot )
    xml_template = xml_template.replace('$$rep:linkagepot$$', linkagepot  )
    xml_template = xml_template.replace('$$rep:namepot$$', namepot )
    xml_template = xml_template.replace('$$rep:descriptionpot$$', descriptionpot )
    xml_template = xml_template.replace('$$rep:functionpot$$', functionpot  )
        
    #===================================================================  metadataConstraints  ===========================================================================================================

    #===========================================================================================================================================================================================================


    xml_template = xml_template.replace('$$rep:useLimitation$$',  useLimitation) #40



    #===================================================================  metadataMaintenance  ===========================================================================================================

    #===========================================================================================================================================================================================================

    xml_template = xml_template.replace('$$rep:maintenanceAndUpdateFrequency$$',  maintenanceAndUpdateFrequency) #41
    xml_template = xml_template.replace('$$rep:updateScope$$',  updateScope) #42
    xml_template = xml_template.replace('$$rep:updateScopeDescription$$',  updateScopeDescription) #43
    xml_template = xml_template.replace('$$rep:maintenanceNote$$',  maintenanceNote) #44
     
       # xml_template = xml_template.replace('$$rep:security$$', restriction)
        #xml_template = xml_template.replace('$$rep:secnote$$', akses)
        #xml_template = xml_template.replace('$$rep:geoserverwms$$', app.config['GEOSERVER_WMS_URL'])
        #xml_template = xml_template.replace('$$rep:geoserverwfs$$', app.config['GEOSERVER_WFS_URL'])
    #except:
        #msg = json.dumps({'MSG':'Metadata tidak sesuai standar!'})
       # print 'Metadata tidak sesuai standar!'

    #print dictxml
    #print xml_template

    # f2 = open('file11.mcf','w')
    # f2.write(xml_template)
    # f2.close()
    # file_xml_template.close()
    # f.close()

    # xml_string = render_template('file11.mcf', schema='iso19139')
    # with open('hasil11.xml', 'w') as ff:
        # ff.write(xml_string)
    # ff.close()

    return xml_template


def parse_metadata_md(input_xml):
    dictxml = xmltodict.parse(input_xml)
    
    #print dictxml

    #metadata
    try:
        datestamp = dictxml["gmd:MD_Metadata"]["gmd:dateStamp"]["gco:DateTime"]
        if datestamp.strip() == None:
            datestamp = '2018-01-01T01:01:01'
        print "datestamp = ", datestamp
    except:
        datestamp = '2018-01-01T01:01:01'
        print "datestamp = ", datestamp

    #Identification Info    
    try:
        layer_title = dictxml["gmd:MD_Metadata"]["gmd:identificationInfo"]["gmd:MD_DataIdentification"]["gmd:citation"]["gmd:CI_Citation"]["gmd:title"]["gco:CharacterString"]
        if layer_title.strip() == None:
            layer_title = "Belum Ada"
        print "layer_title = ", layer_title
    except:
        layer_title = "Belum Ada"
        print "layer_title = ", layer_title

    try:
        keyword=dictxml["gmd:MD_Metadata"]["gmd:identificationInfo"]["gmd:MD_DataIdentification"]["gmd:descriptiveKeywords"]["gmd:MD_Keywords"]["gmd:keyword"]["gco:CharacterString"]
        if keyword.strip() == None:
            keyword = "Lain-lain"
        print "keyword = ", keyword
    except:
        keyword = "Lain-lain"
        print "keyword = ", keyword

    
    #Distributor
    
    try:
        distorganisationName = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:organisationName"]["gco:CharacterString"]
        if distorganisationName.strip() == None:
            distorganisationName = "Belum Ada"
        print "distorganisationName = ", distorganisationName
    except:
        distorganisationName = "Belum Ada"
        print "distorganisationName = ", distorganisationName

    try:
        distindividualName = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:individualName"]["gco:CharacterString"]
        if distindividualName.strip() == None:
            distindividualName = "Belum Ada"
        print "distindividualName = ", distindividualName
    except:
        distindividualName = "Belum Ada "
        print "distindividualName = ", distindividualName

    try:
        distpositionName = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:positionName"]["gco:CharacterString"]
        if distpositionName.strip() == None:
            distpositionName = "Belum Ada"
        print "distpositionName = ", distpositionName
    except:
        distpositionName = "Belum Ada"
        print "distpositionName = ", dispositionName 

    try: 
        distvoice=dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:phone"]["gmd:CI_Telephone"]["gmd:voice"]["gco:CharacterString"]
        if distvoice.strip() == None:
            distvoice = "Belum Ada"
        print "distvoice = ", distvoice
    except:
        voice = "Belum Ada"
        print "distvoice = ", distvoice

    try:
        distfacsimile = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:phone"]["gmd:CI_Telephone"]["gmd:facsimile"]["gco:CharacterString"]
        if distfacsimile.strip() == None:
            distfacsimile = "Belum Ada"
        print "distfacsimile = ", distfacsimile
    except:
        distfacsimile = "Belum Ada"
        print "distfacsimile = ", distfacsimile
    

    try:
        distdeliveryPoint = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:deliveryPoint"]["gco:CharacterString"]
        if distdeliveryPoint.strip() == None:
            distdeliveryPoint = "Belum Ada"
        print "distdeliveryPoint = ", distdeliveryPoint
    except:
        distdeliveryPoint = "Belum Ada"
        print "distdeliveryPoint = ", distdeliveryPoint

    try:
        distcity = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:city"]["gco:CharacterString"]
        if distcity.strip() == None:
            distcity = "Belum Ada"
        print "distcity = ", distcity
    except:
        distcity = "Belum Ada"
        print "distcity = ", distcity

    try:
        distadministrativeArea = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:administrativeArea"]["gco:CharacterString"]
        if distadministrativeArea.strip() == None:
            distadministrativeArea = "Belum Ada"
        print "distadministrativeArea = ", distadministrativeArea
    except:
        distadministrativeArea = "Belum Ada"
        print "distadministrativeArea = ", distadministrativeArea

    try: 
        distpostalCode = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:postalCode"]["gco:CharacterString"]
        if  distpostalCode.strip() == None:
            distpostalCode = "Belum Ada"
        print "distpostalCode = ", distpostalCode
    except:
        distpostalCode = "Belum Ada"
        print "distpostalCode = ", distpostalCode

    try:
        distcountry = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:country"]["gco:CharacterString"]
        if distcountry.strip() == None:
            distcountry = "Belum Ada"
        print "distcountry = ", distcountry
    except:
        distcountry ="Belum Ada"
        print "distcountry = ", distcountry
        
    try:
        distelectronicMailAddress = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:electronicMailAddress"]["gco:CharacterString"]
        if distelectronicMailAddress.strip() == None:
            distelectronicMailAddress = "Belum Ada"
        print "distelectronicMailAddress = ", distelectronicMailAddress
    except:
        distelectronicMailAddress = "Belum Ada"
        print "distelectronicMailAddress = ", distelectronicMailAddress
        
    try: 
        distdataSetURI = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:onlineResource"]["gmd:CI_OnlineResource"]["gmd:linkage"]["gmd:URL"]
        if distdataSetURI.strip() == None:
            distdataSetURI = "Belum Ada"
        print "distdataSetURI = ", distdataSetURI
    except:
        distdataSetURI = "Belum Ada"
        print "distdataSetURI = ", distdataSetURI 
  
    try:
        disthoursOfServiceidentifi2 = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:hoursOfService"]["gco:CharacterString"]
        if disthoursOfServiceidentifi2.strip() == None:
            disthoursOfServiceidentifi2 = "Belum Ada"
        print "disthoursOfServiceidentifi2 = ",  disthoursOfServiceidentifi2 
    except:
        disthoursOfServiceidentifi2 = "Belum Ada"
        print "disthoursOfServiceidentifi2 = ",  disthoursOfServiceidentifi2
     
    try:
        distcontactInstructionsidentifi2 = dictxml["gmd:MD_Metadata"]["gmd:distributionInfo"]["gmd:MD_Distribution"]["gmd:distributor"]["gmd:MD_Distributor"]["gmd:distributorContact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:contactInstructions"]["gco:CharacterString"]
        if  distcontactInstructionsidentifi2.strip() == None:
             distcontactInstructionsidentifi2 = "Belum Ada"
        print  "distcontactInstructionsidentifi2 = ", distcontactInstructionsidentifi2
    except:
         distcontactInstructionsidentifi2 = "Belum Ada"
         print  "distcontactInstructionsidentifi2 = ", distcontactInstructionsidentifi2

    #Contact                  
        
    try:
        individualName = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:individualName"]["gco:CharacterString"]
        if individualName.strip() == None:
            individualName = "Belum Ada"
        print "individualName = ", individualName
    except:
        individualName = "Belum Ada"
        print "individualName = ", individualName
   
    try:
        organisationName = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:organisationName"]["gco:CharacterString"]
        if organisationName.strip() == None:
            organisationName = "Belum Ada"
        print "organisationName = ", organisationName
    except:
        organisationName = "Belum Ada"
        print "organisationName = ", organisationName

    try:
        positionName = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:positionName"]["gco:CharacterString"]
        if positionName.strip() == None:
            positionName = "Belum Ada"
        print "positionName = ", positionName
    except:
        positionName = "Belum Ada"
        print "positionName = ", positionName

    try:
        voice = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:phone"]["gmd:CI_Telephone"]["gmd:voice"]["gco:CharacterString"]
        if voice.strip() == None:
            voice = "Belum Ada"
        print "voice = ", voice
    except:
        voice = "Belum Ada"
        print "voice = ", voice
    
    try:
        facsimile = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:phone"]["gmd:CI_Telephone"]["gmd:facsimile"]["gco:CharacterString"]
        if  facsimile.strip() == None:
            facsimile = "Belum Ada"
        print "facsimile = ", facsimile
    except:
        facsimile = "Belum Ada"
   
    try:
        deliveryPoint = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:deliveryPoint"]["gco:CharacterString"]
        if deliveryPoint.strip() == None:
            deliveryPoint = ""
        print "deliveryPoint = ", deliveryPoint
    except:
        deliveryPoint = "Belum Ada"
        print "deliveryPoint = ", deliveryPoint

     
    
    try:
        city = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:city"]["gco:CharacterString"]
        if city.strip() == None:
            city = "Belum Ada"
        print "city = ", city
    except:
        print "city = ", city

    try:
        administrativeArea = ["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:administrativeArea"]["gco:CharacterString"]
        if administrativeArea.strip() == None:
            administrativeArea = "Belum Ada"
        print "administrativeArea = ", administrativeArea
    except:
        administrativeArea = "Belum Ada"
        print "administrativeArea = ", administrativeArea

    try:
        postalCode = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:postalCode"]["gco:CharacterString"]
        if postalCode.strip() == None:
            postalCode = "Belum Ada"
        print "postalCode = ", postalCode
    except:
        postalCode = "Belum Ada"
        print "postalCode = ", postalCode


    try:
        country = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:country"]["gco:CharacterString"]
        if country.strip() == None:
            country = "Belum Ada"
        print "country =", country
    except:
        country = "Belum Ada"
        print "country =", country

    
    try:
        electronicMailAddress = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:address"]["gmd:CI_Address"]["gmd:electronicMailAddress"]["gco:CharacterString"]
        if electronicMailAddress.strip() == None:
            electronicMailAddress = "Belum Ada"
        print "electronicMailAddress = ", electronicMailAddress
    except:
        electronicMailAddress = "Belum Ada"
        print "electronicMailAddress = ", electronicMailAddress

    
    try:
        dataSetURI = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:onlineResource"]["gmd:CI_OnlineResource"]["gmd:linkage"]["gmd:URL"]
        if dataSetURI.strip() == None:
            dataSetURI = "Belum Ada"
        print "dataSetURI = ", dataSetURI
    except:
        dataSetURI = "Belum Ada"
        print "dataSetURI = ", dataSetURI
   
    try:
        hoursOfServiceidentifi2 = dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:hoursOfService"]["gco:CharacterString"]
        if  hoursOfServiceidentifi2.strip() == None:
            hoursOfServiceidentifi2 = "Belum Ada"
        print "hoursOfServiceidentifi2 = ",  hoursOfServiceidentifi2
    except:
        hoursOfServiceidentifi2 = "Belum Ada"
        print "hoursOfServiceidentifi2 = ",  hoursOfServiceidentifi2
 
    
    try:
        contactInstructionsidentifi2 = (dictxml["gmd:MD_Metadata"]["gmd:contact"]["gmd:CI_ResponsibleParty"]["gmd:contactInfo"]["gmd:CI_Contact"]["gmd:contactInstructions"]["gco:CharacterString"]);
        if contactInstructionsidentifi2.strip() == None:
            contactInstructionsidentifi2 = "Belum Ada"
        print "contactInstructionsidentifi2 = ", contactInstructionsidentifi2
    except:
        contactInstructionsidentifi2 = "Belum Ada"
        print "contactInstructionsidentifi2 = ", contactInstructionsidentifi2
   


    with open(cfg.APP_BASE + 'CP-indonesia.mcf', 'r') as file_mcf_lengkap:
        mcf_lengkap = file_mcf_lengkap.read()

    # template replace
    mcf_lengkap = mcf_lengkap.replace('$$rep:dateStamp$$', datestamp)
    #ident
    mcf_lengkap = mcf_lengkap.replace('$$rep:title$$', layer_title)
    mcf_lengkap = mcf_lengkap.replace('$$rep:keywords$$', keyword)
    #contact
    mcf_lengkap = mcf_lengkap.replace('$$rep:organisationName$$', organisationName)
    mcf_lengkap = mcf_lengkap.replace('$$rep:dataSetURI$$', dataSetURI)
    mcf_lengkap = mcf_lengkap.replace('$$rep:individualName$$', individualName)
    mcf_lengkap = mcf_lengkap.replace('$$rep:positionName$$', positionName)
    mcf_lengkap = mcf_lengkap.replace('$$rep:voice$$', voice)
    mcf_lengkap = mcf_lengkap.replace('$$rep:facsimile$$', facsimile)
    mcf_lengkap = mcf_lengkap.replace('$$rep:deliveryPoint$$', deliveryPoint)
    mcf_lengkap = mcf_lengkap.replace('$$rep:city$$', city)
    mcf_lengkap = mcf_lengkap.replace('$$rep:administrativeArea$$', administrativeArea)
    mcf_lengkap = mcf_lengkap.replace('$$rep:postalCode$$', postalCode)
    mcf_lengkap = mcf_lengkap.replace('$$rep:country$$', country)
    mcf_lengkap = mcf_lengkap.replace('$$rep:electronicMailAddress$$', electronicMailAddress)
    mcf_lengkap = mcf_lengkap.replace('$$rep:hoursOfServiceidentifi2$$', hoursOfServiceidentifi2)
    mcf_lengkap = mcf_lengkap.replace('$$rep:contactInstructionsidentifi2$$', contactInstructionsidentifi2)
    # contact distro
    mcf_lengkap = mcf_lengkap.replace('$$rep:distorganisationName$$', distorganisationName)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distdataSetURI$$', distdataSetURI)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distindividualName$$', distindividualName)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distpositionName$$', distpositionName)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distvoice$$', distvoice)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distfacsimile$$', distfacsimile)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distdeliveryPoint$$', distdeliveryPoint)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distcity$$', distcity)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distadministrativeArea$$', distadministrativeArea)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distpostalCode$$', distpostalCode)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distcountry$$', distcountry)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distelectronicMailAddress$$', distelectronicMailAddress)
    mcf_lengkap = mcf_lengkap.replace('$$rep:disthoursOfServiceidentifi2$$', disthoursOfServiceidentifi2)
    mcf_lengkap = mcf_lengkap.replace('$$rep:distcontactInstructionsidentifi2$$', distcontactInstructionsidentifi2)

    return mcf_lengkap



     # try {
     #                    scope.tanggalku2 = (dictxml["gmd:MD_Metadata"]["gmd:dateStamp"]["gco:DateTime"]);
     #                    scope.tanggalku = new Date(scope.tanggalku2);
     #                }  catch (err) {
     #                    scope.tanggalku = new Date();
     #                }    

     #                console.log(scope.tanggalku);

     #                try {
     #                    scope.layer_id = scope.model.item.identifier; 
     #                } catch (err)
     #                {
     #                    scope.layer_id = (Math.random());
     #                }

     #                console.log(scope.layer_id);

     #                scope.workspace_kugi = scope.model.item.workspace;
                    
     #                console.log(scope.workspace_kugi);

                    

     #                try {
     #                    scope.layer_abstract = (dictxml["gmd:MD_Metadata"]["gmd:identificationInfo"]["gmd:MD_DataIdentification"]["gmd:abstract"]["gco:CharacterString"]); 
     #                } catch (err)
     #                {
     #                    scope.layer_abstract = "Data Tidak Ada";
     #                }
                    
     #                console.log(scope.layer_abstract)

     #                try {
     #                    scope.keyword_item = (dictxml["gmd:MD_Metadata"]["gmd:identificationInfo"]["gmd:MD_DataIdentification"]["gmd:descriptiveKeywords"]["gmd:MD_Keywords"]["gmd:keyword"]["gco:CharacterString"]); 
     #                } catch (err)
     #                {
     #                    scope.keyword_item ="";
     #                }
     #                console.log(scope.keyword_item);

                    
     #                try {
     #                    scope.datausernote =(dictxml["gmd:MD_Metadata"]["gmd:metadataConstrains"]["gmd:MD_SecurityConstraints"]["gmd:userNote"]["gco:CharacterString"]);
     #                } catch (err)
     #                {
     #                    scope.datausernote = "";
     #                } 

     #                  console.log(scope.datausernote);                                                         
                     


     #                scope.akses = {  
     #                        "value": scope.datausernote, 
     #                        "values": [ "PUBLIC", "GOVERNMENT", "PRIVATE", "IGSTRATEGIS"] 
     #                      };

 