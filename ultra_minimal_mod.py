
#!/usr/bin/env python3
import os
import shutil

class UltraMinimalMod:
    def __init__(self):
        # CHỈ thay 1 BYTE duy nhất để test
        self.single_target = {
            "mod/files/Resources/1.59.1/AssetRefs/Hero/150_AssetRef.bytes": [
                (0x40, 84, 120),  # Chỉ 1 vị trí duy nhất
            ]
        }
        
    def backup_file(self, file_path):
        backup_path = f"{file_path}.backup"
        if not os.path.exists(backup_path):
            shutil.copy2(file_path, backup_path)
            print(f"💾 Backup: {os.path.basename(file_path)}")
    
    def single_byte_mod(self, file_path, targets):
        """CHỈ THAY 1 BYTE DUY NHẤT"""
        print(f"\n🔧 TESTING: {os.path.basename(file_path)}")
        
        if not os.path.exists(file_path):
            return False
            
        self.backup_file(file_path)
        
        with open(file_path, 'rb') as f:
            data = bytearray(f.read())
        
        changes = 0
        for offset, old_val, new_val in targets:
            if offset < len(data) and data[offset] == old_val:
                data[offset] = new_val
                print(f"  ✅ 0x{offset:06x}: {old_val} -> {new_val}")
                changes += 1
                break  # CHỈ THAY 1 BYTE
        
        if changes > 0:
            with open(file_path, 'wb') as f:
                f.write(data)
            return True
        return False
    
    def run_test(self):
        print("🧪 ULTRA MINIMAL TEST - CHỈ 1 BYTE")
        print("🎯 Test xem game có chấp nhận thay đổi không")
        print("="*50)
        
        for file_path, targets in self.single_target.items():
            if os.path.exists(file_path):
                success = self.single_byte_mod(file_path, targets)
                if success:
                    print("✅ Test mod applied - check game now")
                else:
                    print("❌ Target byte not found")
            else:
                print(f"❌ File not found: {file_path}")

if __name__ == "__main__":
    mod = UltraMinimalMod()
    mod.run_test()
