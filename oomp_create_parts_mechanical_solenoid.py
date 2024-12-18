import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #casters
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "solenoid"
        part_details["size"] = "" #voltage
        part_details["color"] = ""
        part_details["description_main"] = "" #measurement
        part_details["description_extra"] = "" # lift weight
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        
        part_default = part_details

        
        sizes = ["12_volt", "24_volt"]
        mains = []
        #8,2,300 gram
        mains.append([8,20,300])
        #10,10,300 gram
        mains.append([10,10,300])
        #15,15,500 gram
        mains.append([15,15,500])
        #20,15,3000
        mains.append([20,15,3000])
        #25,20,8000
        mains.append([25,20,8000])
        #60,15 15000
        mains.append([30,15,15000])
        #40,20,30000
        mains.append([40,20,30000])
        #49,21,45000
        mains.append([49,21,45000])
        #50,30,60000
        mains.append([50,30,60000])
        #65,30,85000
        mains.append([65,30,85000])
        #70,10,25000
        mains.append([70,10,25000])
        #80,10,25000
        mains.append([80,10,25000])
        #80,38,120000    
        mains.append([80,38,120000])

        for size in sizes:
            for main in mains:
                part_details = copy.deepcopy(part_default)
                part_details["size"] = f"{size}"
                part_details["description_main"] = f"{main[0]}_mm_diameter_{main[1]}_mm_depth"
                part_details["description_extra"] = f"{main[2]}_gram_capacity"
                part_details["short_name"] = f"Solenoid {main[0]}mm x {main[1]}mm {main[2]/1000}kg {size}"  
                parts.append(part_details)

        



        



    oomp.add_parts(parts, make_files=make_files)
    