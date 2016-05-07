c = get_config()

c.NbConvertApp.notebooks = ['index.ipynb']
c.NbConvertApp.export_format = 'pdf'
c.Exporter.template_file = 'template'
c.PDFExporter.latex_command = ['xelatex', '{filename}']
