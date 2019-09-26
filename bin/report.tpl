<h1> LOG RESULTS REPORT</h1>
<table border="1", bgcolor="green">

%for ip,dt,im,url in res:
%if im == "No Image":
    <tr bgcolor="yellow">
        <td></td>
        <td>{{ip}}</td>
        <td>{{dt}}</td>
        <td bgcolor="red">{{im}}</td>
        <td>{{url}}</td>
    </tr>
%else:
    <tr>
        <td></td>
        <td>{{ip}}</td>
        <td>{{dt}}</td>
        <td >{{im}}</td>
        <td>{{url}}</td>
    </tr>

%end
%end
</table>