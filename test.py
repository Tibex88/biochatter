from biochatter.rag_agent import RagAgent
from biochatter.prompts import BioCypherPromptEngine # from biochatter
# from .prompts import BioCypherPromptEngine # from biochatter
from hyperon import MeTTa
from biochatter.database_agent import DatabaseAgent

metta = MeTTa()
# biochatter code
# use_prompt = use_prompt
# n_results = n_results
# documentids_workspace = documentids_workspace
# last_response = []
model_name = "gpt-3.5-turbo"
# connection_args = []
schema_config_or_info_dict = "./utils/schema_config.yaml"
user_question = "Give me the query to get the name for the compund with CID CID2499366 VALUE "
metta_file = "./utils/test.metta"
# metta_file = "./utils/nodes.metta"

# agent = RagAgent.DatabaseAgent(
#     model_name=model_name, # ✅
#     connection_args=connection_args, # ❌
#     schema_config_or_info_dict=schema_config_or_info_dict, # ✅
#     conversation_factory=conversation_factory, # ❌
# )

# agent.connect() not going to be used

prompt_engine = BioCypherPromptEngine(
            model_name=model_name,
            schema_config_or_info_path=schema_config_or_info_dict,
            # conversation_factory=conversation_factory,
        )

# cypher_query = prompt_engine.generate_query(user_question)

# query_func = agent.get_query_results
# print(cypher_query)

# //////////////////////////////////////////////////////////

# results = query_func(user_question, n_results) # on generate_response
# response = [
# (
#     result.page_content,
#     result.metadata,
# )
# for result in results
# ]
# return response
# print(results)


# Wanted
# !(match &self ($prop (gene ENSG00000290825) $val)
#     ($prop $val))

# Got
# MATCH (c:Compound)-[:HAS_DESCRIPTOR]->(d:Descriptor)
# RETURN c.name, d.name, d.unit, d.source, d.source_url;

# MATCH (c:Compound)-[:HAS_DESCRIPTOR]->(d:Descriptor)
# WHERE c.name = 'Aspirin'
# RETURN c.name, d.name, d.unit, d.source, d.source_url;

# MATCH (c:Compound)-[:HAS_DESCRIPTOR]->(d:Descriptor)
# WHERE c.name = 'IRX3'
# RETURN d.name, d.unit

# (match &self ($prop (Entity Compound) $val)
#     ($prop (Entity Compound) $val))

print(metta.import_file(metta_file))

[[(end 14409), (chr chr1), (gene_type lncRNA), (synonyms (DEAD/H-box_helicase_11_like_1_ 
(pseudogene) DDX11L1 DEAD/H_
 (Asp-Glu-Ala-Asp/His) _box_polypeptide_11_like_1 DEAD/H_box_polypeptide_11_like_1 HGNC:37102 DEAD/H_ 
 (Asp-Glu-Ala-Asp/His) _box_helicase_11_like_1)), (gene_name DDX11L2), (start 11869)]]