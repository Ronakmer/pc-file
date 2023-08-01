

def show_maintenance(request):

    img=[]
    user = User.objects.all()
    user_detail = user_details.objects.filter()
        


    user_property = maintenance.objects.all()
    user_roles = user_role.objects.all()
    rental_detail = rental_details.objects.all()
    client_detail=client_details.objects.all()
    

    images=maintenance_image.objects.all()
    for k in range(0,len(user_property)):
        counter=0
        for i in range(0,len(images)):
            if(user_property[k].pk==images[i].maintenance_image.pk):
                img.append({"count":counter,"maintenance":{"id":images[i].maintenance_image.pk},"images":images[i].images})
                counter=counter+1
    print(img,'kkkkkkkkkkkkkkk')
    

    return render(request,'adminTemplate/maintenance.html',{'baseURL':baseUrl,'rental_detail':rental_detail,'user_property':user_property,'user_roles':user_roles,'img':img,'user':user,'images':images,'client_detail':client_detail})





def add_maintenance(request):
    dealerid=request.POST.get('userid')

    print(dealerid,'0000000000000000000')
    issue_title = request.POST.get('issue_title')
    issue_details = request.POST.get('issue_details')
    date = request.POST.get('date')
    time = request.POST.get('time')
    issue_address = request.POST.get('issue_address')
    images = request.FILES.getlist('maintenance_image')
    

    # dealerid = user_role.objects.get(id=dealerid)
    # print(userdata,'44444444444444444444444')
 
    logUser = maintenance()
    logUser.issue_title = issue_title  # connect tabel
    logUser.user = dealerid
    logUser.issue_details = issue_details
    logUser.time = time
    logUser.date = date
    logUser.issue_address = issue_address
    logUser.save()




    obj=maintenance.objects.get(issue_title=issue_title)
    # obj_img=Image()
    for i in images:
        maintenance_image.objects.create(maintenance_image=obj,images=i)

    messages.success(request, 'property add')


    return redirect('show_maintenance')


def delete_maintenance(request, id):
    upuser = maintenance.objects.get(id=id)
    print(upuser,'00000000000000000000000000')
    upuser.delete()
    return redirect('show_maintenance')





def Update_maintenance(request, id):
    upuser=maintenance.objects.get(id=id)
    if request.method=='POST':
        upuser.user = request.POST.get('userid')
        upuser.issue_title = request.POST.get('issue_title')
        upuser.issue_details = request.POST.get('issue_details')
        upuser.date = request.POST.get('date')
        upuser.time = request.POST.get('time')

        upuser.save()

        property_images = maintenance_image.objects.all()
        try:
            img=request.FILES.getlist('images')
            print(img,'888888888888888888888888888888')
            print(len(img))
            if(len(img)!=0):
                for k in property_images:
                    if(k.maintenance_image.pk==id):
                        obj_del=maintenance_image.objects.get(id=k.pk)
                        obj_del.delete()
                for j in img:
                    maintenance_image.objects.create(property_image=i,images=j)
            else:
                for i in property_images:
                    if(i.maintenance_image.pk==id):
                        try:
                            img=request.FILES[f'images-{i.pk}']
                            obj_img=maintenance_image.objects.get(id=i.pk)
                            obj_img.images=img
                            obj_img.save()
                        except Exception as e:
                            print(e,'llllllllllllllll')
        except Exception as e:
            print(e,'jjjjjjjjjjjj')



        messages.success(request, 'maintenance update')
        return redirect('show_maintenance')
    else:
        
        return render(request,'404.html')
        
        
####################################################################################################



class maintenance(models.Model):
    # user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    user = models.CharField(max_length=30, default="")
    issue_title = models.CharField(max_length=30, default="")
    issue_details = models.CharField(max_length=100, default="")
    issue_address = models.CharField(max_length=100, default="")
    # issue_img =models.FileField(upload_to="home/img", default="")
    status=models.CharField(max_length=20, default="True")
    date=models.DateField(default=timezone.now)
    time=models.TimeField(default=timezone.now)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)



class maintenance_image(models.Model):
    maintenance_image = models.ForeignKey(maintenance, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="home/img")


#####################################################################################################

{% extends 'adminTemplate/base.html' %}

{% load static %}

{% block body  %}

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/css/lightbox.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/js/lightbox.min.js"></script>



<div class="container">
    <table class="table table-dark table-striped">
        <div class="container">
            <div class="row">
                <div class="col-sm-8" style="margin-top: 10px; margin-left:
                    -15px; ">
                    <h3><b>Maintenance </b></h3>
                </div>
                <div class="col-sm-4 text-end">

                    <div>
                        <a href='' class="btn btn-primary" style=" padding: 12px
                            34px; margin-top: 10px; margin-right: -38px;" data-toggle="modal" data-target="#addModal"> <i class="fa-solid fa-plus"></i> Add New</a>

                    </div>
                </div><br><br>
                <div class="col-13">
                    <table class="table table-bordered mt-3">
                        <thead>
                            <tr>
                                <th scope="col">Sno.</th>
                                <th scope="col" class="w-10">User</th>
                                <th scope="col">Maintenance Title</th>
                                <th scope="col">Maintenance Details</th>
                                <th scope="col">Maintenance Images</th>
                                <th scope="col">Maintenance Date</th>
                                <th scope="col">Maintenance Time</th> 
                                {% comment %} <th scope="col">Property Dealer</th> 
                                <th scope="col">Property Owner Name</th>  {% endcomment %}
                                <th scope="col">Maintenance Address</th>

                                <th scope="col">Update</th>
                                <th scope="col">Delete</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                {% for data in user_property %}
                                {% comment %} {{}} {% endcomment %}
                                <th scope="row">{{forloop.counter}}</th>
                                <th scope="row">{{data.user}}</th>


                                <td scope="row">{{data.issue_title}}</td>
                                <td scope="row">{{data.issue_details}}</td>
                                {% comment %} <td scope="row">{{data.property_images}}</td> {% endcomment %}
                              
                                
                                    {% comment %} <div class="photo-gallery">
                                        <div class="row photos"> {% endcomment %}
                                            {% comment %} |slice:":1" {% endcomment %}


  
                            <td>
                                                     
                                <div class="photo-gallery">
                                    <div class="row photos">
                                        {% comment %} |slice:":1" {% endcomment %}
                                        
                                        {% for k in img %}
                                        {% comment %} {{k.property.id}}sdfsd {% endcomment %}
                                
                                {% if k.maintenance.id == data.id %}   
                                {% if k.count == 0 %}  

                                {% comment %} <img src="{{k.images.url}}" class="card-img-top"  alt="category image" style="height: 20%; width: 200%;}">                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {% endcomment %}
                                <div class="item"><a href="{{k.images.url}}" data-lightbox="photos"><img class="img-fluid" src="{{k.images.url}}"></a></div>
                                {% else %}
                                <div class="item" hidden><a href="{{k.images.url}}" data-lightbox="photos"><img class="img-fluid" src="{{k.images.url}}"></a></div>
                                {% endif %}      
                            
                                    

                                {% endif %}    
                                {% endfor %}
                                
                                    </div></div></td>
                                            
                                <td scope="row">{{data.date}}</td>

                                <td scope="row">{{data.time}}</td>
                                <td scope="row">{{data.issue_address}}</td>

                                {% comment %} <td scope="row">{{data.owner_name}}</td>
                                <td scope="row">{{data.property_rental}}</td>
                                
                                onClick=myfun(zxxcxcxcx,sd,ds,ds )
                                {% endcomment %}

                               
                                <td>
                                    <a href="#updModal-{{forloop.counter}}"  class="btn btn-success" data-toggle="modal"><i class="fa-regular fa-pen-to-square"></i>
                                    </a>
                                </td>

                                <td> 
                                    <a href="{% url 'delete_maintenance' data.id %}" onclick="return confirm('Are You Sure,You want to delete this data?');" class="btn btn-danger"><i class='fas fa-trash-alt'></i>
                                    </a> 
                                </td>

                            </tr>
                            {%endfor%}


                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </table>
</div>


{% comment %} {{response}} {% endcomment %}
{% comment %} {% for data in response %}
{{data.username}}
{{data.property_name}}
{% endfor %} {% endcomment %}

{% comment %} ---------------------------------------------------------------ADD MODAL------------------------------------------------------------------------------- {% endcomment %}
<div class="modal fade" id="addModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Maintenance</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span> 
                </button>
            </div>
            <div class="modal-body">
                {% comment %} <form action="http://192.168.0.110:8000/add_property/" method="post"> {% endcomment %}
                    <form action="/add_maintenance/" method="post" enctype="multipart/form-data">

                    {% csrf_token%}
                    {% comment %} <div class="form-group">
                        <label for="exampleFormControlSelect1">Dealer Name:</label>
                        <select class="form-control" name='dealerid' id="user">
                        {% for data in client_detail %}
                                    <option value='{{data.user.username}}' >{{data.user.username}}</option>
                                {% endfor %}
                            </select><br> {% endcomment %}

                       {% comment %} <label for="exampleFormControlSelect1">User Name:</label>
                        <select class="form-control" name='userid' id="user">
                        {% for data in client_detail %}
                                    <option value='{{data.user.username}}' >{{data.user.username}}</option>
                                {% endfor %}
                            </select><br> {% endcomment %}

                         
                        <label for="recipient-name" class="col-form-label">User Name:</label>   
                        <input type="text" class="form-control" id="recipient-name" required name="userid"><br>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance title:</label>   
                        <input type="text" class="form-control" id="recipient-name" required name="issue_title"><br>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance Details:</label>   
                        <textarea  class="form-control" id="reviewDescription" required name="issue_details" ></textarea><br>


                        <label for="recipient-name" class="col-form-label">Maintenance Address:</label>   
                        <textarea  class="form-control" id="reviewDescription" required name="issue_address" ></textarea><br>
                            
                        <label for="recipient-name" class="col-form-label">Maintenance Images:</label>   
                        <input type="file" class="form-control" id="recipient-name" multiple required name="maintenance_image"><br>
                
          
                        <label for="recipient-name" class="col-form-label">Maintenance Date:</label>                         
                        <input type="date"  class="form-control" id="reviewDescription"  name="date" required></textarea><br>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance Time:</label>                         
                        <input type="time"  class="form-control" id="reviewDescription"  name="time" required></textarea><br>
                        
                        
                        


                        {% comment %} <label for="recipient-name" class="col-form-label">Property Dealer:</label>   
                        <input type="text" class="form-control" id="recipient-name" required name="property_dealer"><br>  {% endcomment %}
                                                
                        <div class="modal-footer " style=" margin-bottom: -36px;
                            margin-right: -24px;">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <button type="Submit" class="btn btn-primary">Submit</button>
                        </div>


                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<script>

    {% comment %} function switchFunction(id, status){
        
        window.location.href=`{{baseURL}}/changeStatusofffercard/${id}`;
    }
    function myfun(){

    } {% endcomment %}
</script>
{% comment %} -----------------------------------------------------------Update Modal------------------------------------------------------------------------------------------ {% endcomment %}
{% for i in user_property%}

<div class="modal fade" id="updModal-{{forloop.counter}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Property Masters</h5>
                <type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>

            </div>
            <div class="modal-body">
                <form action="/Update_maintenance/{{i.id}}" method="post" enctype="multipart/form-data">
                    {% csrf_token%}
                    <div class="form-group">
{% comment %} 
                        <label for="recipient-name" class="col-form-label">Owner Name:</label>   
                        <input type="text" class="form-control" id="recipient-name" required name="owner_name" value="{{i.owner_name}}"  ><br> {% endcomment %}

                        <label for="recipient-name" class="col-form-label">User Name:</label>   
                        <input type="text" class="form-control" id="recipient-name" required name="userid" value="{{i.user}}" ><br>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance title:</label>   
                        <input type="text" class="form-control" id="recipient-name" required name="issue_title" value="{{i.issue_title}}" ><br>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance Address:</label>   
                        <textarea  class="form-control" id="reviewDescription" required name="issue_details"  value="{{i.issue_details}}" >{{i.issue_details}}</textarea><br>
                            
                        {% comment %} <label for="recipient-name" class="col-form-label">Maintenance Images:</label>   
                        <input type="file" class="form-control" id="recipient-name" multiple required name="maintenance_image"><br> {% endcomment %}
                
          
                        
                        <div class='d-flex '>
                            {% for k in images %}
                            {% if k.maintenance_image.id == i.id %}
                            <div class='container pt-0 '>
                            <img src="{{k.images.url}}" class=" card-img-top " alt="category image" style="top: 0; "><br><br>
                            {% comment %} <input type="file" class="form-control" id="images"  name="images-{{k.id}}" text="Change"> {% endcomment %}
                            <input type="file" id="images-{{k.id}}" name="images-{{k.id}}"  hidden/>
                            <label class='lbl' for="images-{{k.id}}" >Change</label> 
                            {% comment %} <input type="file" id="images-{{k.id}}" name="images-{{k.id}}" />
                            <label for="images-{{k.id}}" name="images-{{k.id}}" >Choose File</label> {% endcomment %}
                                 
                        </div>
                            {% endif %}
                            {% endfor %}
                        </div>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance Date:</label>                         
                        <input type="date"  class="form-control" id="reviewDescription"  name="date" value="{{i.date}}"  required><br>
                        
                        <label for="recipient-name" class="col-form-label">Maintenance Time:</label>                         
                        <input type="time"  class="form-control" id="reviewDescription"  name="time" value="{{i.time}}"  required><br>
                          
            

                       
                        {% comment %} <label for="recipient-name" class="col-form-label">Propety Dealer</label>                          
                        <input type="text" class="form-control" id="reviewRating"  name="property_dealer" required value="{{i.property_dealer}}" ><br> {% endcomment %}
                        
                        <div class="modal-footer " style=" margin-bottom: -36px;
                        margin-right: -24px;">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="success" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>



{%endfor%}




{% endblock body  %}
    

