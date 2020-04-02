'''
File name: cdm.py
    Common Data Model Schema Extraction class.
           
Author: Vasileios Saveris
email: vsaveris@gmail.com

License: MIT

Date last modified: 03.04.2020

Python Version: 3.7
'''

import json

class CDM():
    '''
    CDM Schema Extraction class implementation.

    Args:
        path (string): The cdm.json file from which the schema should be 
            extracted.

        core_path (string): The core path of the CDM directory 
            (i.e. ./CDM/schemaDocuments/core)
            
        base_path (string): The base path of the CDM directory 
            (i.e. ./CDM/schemaDocuments/applicationCommon)

    Public Attributes:
        -
        
    Private Attributes:
        See constructor (self._*)
                                
    Public Methods:
        
        getSchema() -> dictionary: Returns the extracted schema in a dictionary
            where key is the attribute name and value is the attribute type.
            
        printSchema() -> None: Prints the schema in a formatted way.
        
    Private Methods:
        See methods docstring (def _*)
        
    Raises:
        ValueError: In case input cdm.json file was not found.
        
    '''

    def __init__(self, path, core_path = None, base_path = None):
    
        print('\nCDM class, path = ', path, ', core_path = ', core_path, 
            ', base_path = ', base_path, sep = '')
        
        # Core document (reference is not sure yet)
        self._core_document = core_path + 'wellKnownCDSAttributeGroups{Version}.cdm.json'
        
        # Read the contents of the CDM file
        self._cdm_file = self._readCdmFile(path)
        
        # Read document id (dictionary with keys: entityName, extendsEntity, 
        # versionNumber)
        self._cdm_id = self._readDocumentId()
        
        if self._cdm_id['entityName'] is None:
            raise ValueError('Entity Name was not found in the CDM file.')
            
        print('Document ID: ', self._cdm_id, sep = '')
        
        # Initialize the Core reference file
        self._core_file = None
        
        # Create schema, first read attributes from the reference entity if 
        # defined and afterwards read attributes from the document itself
        self._schema = {}
        
        # Parse base document
        if self._cdm_id['extendsEntity'] is not None and \
            'base' in self._cdm_id['extendsEntity']:
            
            if self._cdm_id['versionNumber'] is not None:
                base_document = base_path + self._cdm_id['extendsEntity'].split('/')[-1] + \
                    '.' + self._cdm_id['versionNumber'] + '.cdm.json'
            else:
                base_document = base_path + self._cdm_id['extendsEntity'].split('/')[-1] + \
                    '.cdm.json'

            self._schema.update(CDM(base_document, core_path).getSchema())
            
        # Parse core document
        elif self._cdm_id['extendsEntity'] is not None:
            self._schema.update(self._readCoreAttributes(
                self._cdm_id['extendsEntity']))
            
        self._schema.update(self._readDocumentAttributes())
    
    
    def getSchema(self):
        '''
        Returns a dictionary with the extracted schema (getter).
    
        Args:
            -

        Raises:
            -

        Returns:
            dictionary: Returns the extracted schema in a dictionary where key 
                is the attribute name and value is the attribute type.
        '''
        
        return self._schema 

    
    def printSchema(self):
        '''
        Prints the schema in a formatted way.
    
        Args:
            -

        Raises:
            -

        Returns:
            -
        '''
        
        print('\nNumber of attributes in the schema ', 
            self._cdm_id['entityName'], ', version ', 
            self._cdm_id['versionNumber'], ': ', 
            len(self._schema.keys()), sep = '')
    
        max_key_len = len(max(self._schema.keys(), key = len))
        index_len = len(str(len(self._schema.keys())))
        
        i=1
        for k, v in self._schema.items():
            print('{:{}d}. {:{}} : {}'.format(i, index_len, k, max_key_len, v))
            i += 1
    
    
    def _readCoreAttributes(self, core_entity):
        '''
        Extracts schema from the core document for the core entities referenced
        in the cdm.json file.
    
        Args:
            core_entity (string): The core entity references in the cdm.json
                file.

        Raises:
            -

        Returns:
            dictionary: Extracted schema.
        '''
        
        print('\nRead attributes of the core_entity = ', core_entity, sep = '')

        # Load core file
        core_file_path = self._core_document.replace('{Version}', '.' + 
            self._cdm_id['versionNumber'] if self._cdm_id['versionNumber'] is 
            not None else '')
        
        print('- Core file path: ', core_file_path, sep = '')
        
        self._core_file = self._readCdmFile(core_file_path)
        
        # Read attributes of the core entity
        attributes = None
        for item in self._core_file['definitions']:
            
            try:
                if item['entityName'] == core_entity:
                    attributes = item['hasAttributes']
                    break
            except:
                pass
        
        print('- Attributes: ', attributes, sep = '')
        
        # Read schema for the selected attributes
        schema = {}
        
        if attributes is not None:
            for item in self._core_file['definitions']:
                
                try:
                    if item['attributeGroupName'] in attributes:
                        print('- Parsing members of ', item['attributeGroupName'], 
                            sep = '')
                        schema.update(self._parseMembers(item['members']))
                except:
                    pass
        
        return schema
        
        
    def _readDocumentAttributes(self):
        '''
        Extracts schema from the cdm.json for the local attributes.
    
        Args:
            -

        Raises:
            -

        Returns:
            dictionary: Extracted schema.
        '''
        
        print('\nRead attributes of the document, parsing members.')

        return self._parseMembers(self._cdm_file['definitions'][0]
            ['hasAttributes'][0]['attributeGroupReference']['members'])
        
        
    def _parseMembers(self, members):
        '''
        Parses the members of the input members object (cdm decoding).
    
        Args:
            members (dictionary): The members part from a cdm.json file.

        Raises:
            -

        Returns:
            dictionary: Extracted members.
        '''
        
        schema = {}
        
        for m in members:
        
            # Attribute is defined in the core document, search for it
            if isinstance(m, str) and self._core_file is not None:
                for d in self._core_file['definitions']:
                    try:
                        if d['attributeGroupName'] == m:
                            m = d['members'][0]
                            break
                    except:
                        pass

            # Check and parse for entities
            try:
                a_name = m['name']
                a_type = m['dataType'] 
                
                # If type is a dictionary, parse it for the type
                if not isinstance(a_type, str):
                    a_type = a_type['dataTypeReference']  
                
                schema[a_name] = a_type
            except:
                pass
            
            # Check and parse for resolution guidance
            try:
                resolution_guidance = m['resolutionGuidance']
            
                try:
                    # Resolution guidance is entity by reference
                    rg = resolution_guidance['entityByReference']
                    a_name = rg['foreignKeyAttribute']['sourceName']
                    a_type = rg['foreignKeyAttribute']['dataType']
                    schema[a_name] = a_type
                except:
                    pass
                    
                try:
                    # Resolution guidance is selects sub attribute
                    rg = resolution_guidance['selectsSubAttribute']
                    a_name = rg['selectedTypeAttribute']['name']
                    a_type = rg['selectedTypeAttribute']['dataType']
                    schema[a_name] = a_type
                except:
                    pass
                
                # Resolution guidance is add supporting attribute
                try:
                    rg = resolution_guidance['addSupportingAttribute']
                    a_name = rg['name']
                    a_type = rg['dataType']
                    schema[a_name] = a_type
                except:
                    pass
                    
            except:
                pass
                    
        return schema
        
        
    def _readDocumentId(self):
        '''
        Reads the identification part of a cdm.json file. Searches for 
            'entityName', 'extendsEntity' and 'versionNumber' values.
    
        Args:
            -

        Raises:
            -

        Returns:
            dictionary: Values found for the 'entityName', 'extendsEntity' and 
                'versionNumber' attributes.
        '''
        
        en = self._cdm_file['definitions'][0].get('entityName', None)
        ee = self._cdm_file['definitions'][0].get('extendsEntity', None)
        
        # Look for the version number
        version = None
        for t in self._cdm_file['definitions'][0].get('exhibitsTraits', None):
            
            if t['traitReference'] == 'is.CDM.entityVersion':
                try:
                    version = t['arguments'][0]['value']
                    break
                    
                except:
                    pass
                    
        return {'entityName': en, 'extendsEntity': ee, 'versionNumber': version}
    
    
    def _readCdmFile(self, path):
        '''
        Loads a cdm.json file using the json python library.
    
        Args:
            path: The cdm.json file to be loaded.

        Raises:
            -

        Returns:
            object: The loaded file.
        '''
        
        with open(path) as f:
            return json.load(f)
