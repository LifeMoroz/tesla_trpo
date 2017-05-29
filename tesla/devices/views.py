from tesla.devices.models import Device


class Con_TableModule_Devices:
    def create(self, request):
        Device.objects.create(
            name=request.POST['name'],
            state=request.POST['state'],
        )

    def update(self, request):
        Device.objects.get(id=request.POST['id']).update(
            name=request.POST['name'],
            state=request.POST['state'],
        )

    def delete(self, request):
        Device.objects.delete(id=request.POST['id'])
