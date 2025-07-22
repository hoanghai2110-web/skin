
#!/usr/bin/env python3
import os
import shutil

def quick_restore():
    print("🔄 QUICK RESTORE FROM BACKUP")
    
    files_to_restore = [
        "mod/files/Resources/1.59.1/AssetRefs/Hero/150_AssetRef.bytes",
        "mod/files/Resources/1.59.1/Prefab_Characters/Actor_150_Infos.pkg.bytes"
    ]
    
    for file_path in files_to_restore:
        backup_path = f"{file_path}.backup"
        
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, file_path)
            print(f"✅ Restored: {os.path.basename(file_path)}")
        else:
            print(f"❌ No backup: {os.path.basename(file_path)}")
    
    print("🎮 Files restored - test game now")

if __name__ == "__main__":
    quick_restore()
