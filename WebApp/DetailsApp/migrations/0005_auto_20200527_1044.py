# Generated by Django 3.0.3 on 2020-05-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetailsApp', '0004_auto_20200518_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='GraphValue',
            field=models.CharField(blank=True, choices=[('1', 'Pie chart'), ('4', 'Line chart'), ('5', 'Y-axis Bar Chart'), ('6', 'Bubble Chart'), ('7', 'Scatter Plot'), ('8', 'Area Chart'), ('9', 'Donut Graph'), ('10', 'Xaxis Barchart'), ('11', 'TreeMap'), ('12', 'Gauge Chart'), ('14', 'Histogram')], max_length=1200),
        ),
    ]