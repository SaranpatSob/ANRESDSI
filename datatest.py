from firebase import firebase
import random
firebase = firebase.FirebaseApplication(
    'https://test-database-anres.firebaseio.com', None)


# for i in range(10):
#     new_user = str(input())
#     result = firebase.put('/users/'+str(i+1),name = "Tel",data = new_user)
result = firebase.delete('/users', "19-04-07-13-00")
# print(result)
# name = []
# age = []
# tel = []

#     print ("-----------------------------------\n")






# for Info in result:
#     if "Name" in result[Info]:
#         print(result[Info]["Name"])
# for i in result:
#         print(i)

# {% for i in count %}
#     <p>Name : {{name[i]}}</p>
#     <p>Age : {{age[i]}}</p>
#     <p>Tel : {{tel[i]}}</p>
#     <hr>
#     {%endfor%}

# <div class="form-group">
#             <label for="Type">สืบค้นข้อมูลด้วย</label>
#             <select class="form-control" name="searchwhat">
#                 <option value="ค้นหาด้วยชื่อของผู้แจ้ง">Facebook</option>
#                 <option value="ค้นหาด้วยชื่อผู้ต้องสงสัย">E-mail</option>
#                 <option value="ค้นหาด้วยคดี">Line</option>
#                 <option value="ค้นหาด้วยวันที่แจ้ง">Website</option>
#                 <option value="ค้นหาด้วยประเภท">Website</option>
#             </select>
#         </div>
#         <a href="" class="btn btn-warning btn-xs" data-toggle="modal" data-target="#modaledit{{ searchwhat }}">Edit</a>
#         <div id="modaledit{{searchwhat}}" class="modal fade" role="dialog">
#             <div class="modal-dialog">
#                 <div class="modal-content">
#                     <div class="modal-header">
#                         <button type="button" class="close" data-dismiss="modal">&times;</button>
#                         <h4 class="modal-title">ค้นหาข้อมูล</h4>
#                     </div>
#                     <div class="modal-body">
#                         <form action="/ShowSearch" method="POST">
#                             <div class="form-group">
#                                 <label>ฟหกฟดฟหดฟดฟ</label>
#                                 <input type="hidden" name="id" value="{{searchwhat}}">
#                                 <input type="text" class="form-control" name="search" value="">
#                             </div>
#                             <div class="form-group">
#                                 <button class="btn btn-primary" type="submit">ค้นหา</button>
#                             </div>
#                         </form>
#                     </div>
#                     <div class="modal-footer">
#                         <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
#                     </div>
#                 </div>
#             </div>
#         </div>