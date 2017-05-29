from tesla.jobs.models import Job


class Con_TableModule_Jobs:
    def create(self, request):
        Job.objects.create(
            device=request.POST['device'],
            today=request.POST['today'],
            month=request.POST['month'],
            quart=request.POST['quart'],
            half_year=request.POST['half_year'],
            year=request.POST['year'],
        )

    def update(self, request):
        Job.objects.get(id=request.POST['id']).update(
            device=request.POST['device'],
            today=request.POST['today'],
            month=request.POST['month'],
            quart=request.POST['quart'],
            half_year=request.POST['half_year'],
            year=request.POST['year']
        )

    def delete(self, request):
        Job.objects.delete(id=request.POST['id'])
