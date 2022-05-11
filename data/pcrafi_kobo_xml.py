import untangle

path = "aicRLmhkeZNyNYXLjhxDhH.xml"
doc = untangle.parse(path)

groups =  doc.html.body.group
#print(len(groups))

for g in groups:
    model_name = g.label.cdata
    print(" ")
    print(model_name)
    print("=========================================")

    model_name = model_name.replace(" - ", "_")
    print(f"class {model_name}(models.Model):")

    try:

        #select 
        fields = g.select
        for f in fields:
            field_name = f.label.cdata
            #values
            value_list = []
            items = f.item
            for i in items:
                value = i.label.cdata
                value = value.replace(" ", "_").replace("/", "_").replace("-", "_").replace(",", "_").upper()
                value_list.append(value)
            #print(field_name + " : " + str(value_list))
            field_name = field_name.replace(" ", "_").replace("/", "_").lower()
            str_list = ' '.join(value_list)
            print(f"  {field_name}_type = models.TextChoices('{field_name}_type', '{str_list}')")
            print(f"  {field_name} = models.CharField(blank=True, choices={field_name}_type.choices, max_length=255)")

        #text
        fields = g.input
        for f in fields:
            field_name = f.label.cdata
            #print(field_name)
            field_name = field_name.replace(" ", "_").replace("/", "_").lower()
            print(f"  {field_name} = models.CharField(max_length=255)")

        #population
        fields = g.group
        for fg in fields:
            field_name = fg.label.cdata
            #print(field_name + " : ")
            fields = fg.select
            for f in fields:
                pop_field_name = f.label.cdata
                #values
                value_list = []
                items = f.item
                for i in items:
                    value = i.label.cdata
                    value = value.replace(" ", "_").replace("/", "_").replace("-", "_").replace(",", "_").upper()
                    value_list.append(value)
                #print(field_name + " : " + pop_field_name + " : " + str(value_list))
                pop_field_name = field_name.lower() + "_" + pop_field_name.replace(" ", "_").replace("/", "_").lower()
                str_list = ' '.join(value_list)
                print(f"  {pop_field_name}_type = models.TextChoices('{pop_field_name}_type', '{str_list}')")
                print(f"  {pop_field_name} = models.CharField(blank=True, choices={pop_field_name}_type.choices, max_length=255)")
            
            fields = fg.input
            for f in fields:
                pop_field_name = f.label.cdata
                #print(field_name + " : " + pop_field_name)
                pop_field_name = field_name.lower() + "_" + pop_field_name.replace(" ", "_").replace("/", "_").lower()
                print(f"  {pop_field_name} = models.CharField(max_length=255)")

                

                


    except Exception as e:
        #print(e)
        pass


