import chromadb

client = chromadb.PersistentClient(path="data/09_chromadb")
coll = client.get_collection("qwen3_text")

# Lấy các record có metadata source = 'instructor_upload'
res = coll.get(where={"source": "instructor_upload"}, include=["documents", "metadatas"])

print(f"Tổng số bản ghi do Giảng viên vừa nạp trong ChromaDB: {len(res['ids'])}")
print("=" * 80)
for i, (cid, doc, meta) in enumerate(zip(res["ids"], res["documents"], res["metadatas"]), start=1):
    print(f"[{i}] Chunk ID : {cid}")
    print(f"    Tên file : {meta.get('filename')}")
    print(f"    Chủ đề   : {meta.get('topic')}")
    print(f"    Thời gian: {meta.get('created_at')}")
    print(f"    Trích đoạn: {doc[:150].strip().replace(chr(10), ' ')}...")
    print("-" * 80)
