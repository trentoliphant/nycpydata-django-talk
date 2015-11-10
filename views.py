import xlrd
import pandas as pd
from django.shortcuts import render
from django.db import connection, IntegityError, DatabaseError

def upload_data(request):
    if request.method == 'POST':
        workbook = self.open_workbook(request.FILES['uploaded_file'])
        for sheetname in workbook.sheet_name:
            # Do some error checking
            df = pd.read_excel(workbook, sheetname, engine='xlrd')
            cols = ', '.join(df.columns)
            # Django wrapper of the cx_oracle connector expects %s format
            val_holder = ', '.join(['%s'])*len(df.columns)
            stmt_text = "INSERT INTO {} ({}) VALUES {()}"
            stmt = stmt_text.format(sheetname, cols, val_holder)
            cursor = connection.cursor()
            cursor.executemany(stmt, df.values.to_list())
    return render(request, 'upload.html')



import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

def download_file(request):
    filepath = 'Newly created file'
    wrapper = FileWrapper(open(filepath, 'rb'))
    response = HttpResponse(wrapper, content_type='application/force-download')
    response['Content-Length'] = os.path.getsize(filepath)
    filename = os.path.basename(filepath)
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response