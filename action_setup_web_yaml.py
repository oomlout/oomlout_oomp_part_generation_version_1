import oomp
import oom_git

def main(**kwargs):
    filter = kwargs.get("filter", "")
    

    yanml_file_folder = r"C:\gh\oomp_part_generation_1_web_interface\parts_source"

    parts = []

    
    
    
    make_files = kwargs.get("make_files", True)

    #load all the yaml files in 
    import glob
    import os
    import yaml
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the script directory to ensure parts are created in the right location
    original_dir = os.getcwd()
    os.chdir(script_dir)
    
    print("=" * 80)
    print("🎯 OOMP Part Setup - Web YAML")
    print("=" * 80)
    print(f"\n📂 Script location: {script_dir}")
    print(f"📂 Working directory set to: {script_dir}")
    
    yaml_files = glob.glob(os.path.join(yanml_file_folder, "*.yaml"))
    print(f"\n📁 Found {len(yaml_files)} YAML file(s) in: {yanml_file_folder}")
    
    # Track statistics
    total_parts_found = 0
    new_parts = 0
    existing_parts = 0
    # Parts folder is now always relative to the script location
    parts_folder = os.path.join(script_dir, "parts")
    print(f"📂 Parts will be saved to: {parts_folder}")
    
    print("\n🔍 Checking which parts are new vs. existing...")
    print("-" * 80)
    
    for yaml_file in yaml_files:
        filename = os.path.basename(yaml_file)
        print(f"\n📄 Processing: {filename}")
        
        with open(yaml_file, 'r') as f:
            yaml_parts = yaml.safe_load(f)
            
            if yaml_parts is None:
                print(f"   ⚠️  Empty file, skipping...")
                continue
                
            total_parts_found += 1
            
            # Generate part ID to check if it exists
            # Use the same logic as get_id from oomp.py
            part_id = ""
            
            # Build the ID from part components
            if isinstance(yaml_parts, dict):
                classification = yaml_parts.get("classification", "")
                type_val = yaml_parts.get("type", "")
                size = yaml_parts.get("size", "")
                color = yaml_parts.get("color", "")
                description_main = yaml_parts.get("description_main", "")
                description_extra = yaml_parts.get("description_extra", "")
                manufacturer = yaml_parts.get("manufacturer", "")
                part_number = yaml_parts.get("part_number", "")
                
                # Build part_id the same way as in oomp.get_id
                part_id_components = []
                if classification:
                    part_id_components.append(classification)
                if type_val:
                    part_id_components.append(type_val)
                if size:
                    part_id_components.append(size)
                if color:
                    part_id_components.append(color)
                if description_main:
                    part_id_components.append(description_main)
                if description_extra:
                    part_id_components.append(description_extra)
                if manufacturer:
                    part_id_components.append(manufacturer)
                if part_number:
                    part_id_components.append(part_number)
                    
                part_id = "_".join(part_id_components)
            
            # Check if part already exists in parts folder
            if part_id:
                part_path = os.path.join(parts_folder, part_id)
                if os.path.exists(part_path) and os.path.isdir(part_path):
                    print(f"   ✓ Already exists: {part_id}")
                    print(f"   ⏭️  Skipping (already in parts folder)")
                    existing_parts += 1
                else:
                    print(f"   ✨ NEW PART: {part_id}")
                    print(f"   ➕ Adding to processing queue")
                    parts.append(yaml_parts)
                    new_parts += 1
            else:
                print(f"   ⚠️  Could not determine part ID, skipping...")
    
    print("\n" + "=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print(f"Total YAML files processed:  {total_parts_found}")
    print(f"New parts to add:            {new_parts} ✨")
    print(f"Existing parts (skipped):    {existing_parts} ⏭️")
    print("=" * 80)
    
    if new_parts > 0:
        print(f"\n⚙️  Processing {new_parts} new part(s)...")
        oomp.add_parts(parts, make_files=make_files)
        
        print("\n💾 Saving parts...")
        oomp.save_parts()
        
        print("📝 Saving individual YAML files...")
        oomp.save_parts_to_individual_yaml_files()
        
        print("\n✅ COMPLETE! All new parts have been added successfully!")
    else:
        print("\n✓ No new parts to add. All parts already exist in the parts folder!")
    
    # Restore original working directory
    os.chdir(original_dir)
    
    print("=" * 80)



    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    kwargs = {}

    filter = ""

    kwargs["filter"] = filter
    main(**kwargs)
