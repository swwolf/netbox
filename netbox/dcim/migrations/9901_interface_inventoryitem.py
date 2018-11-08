from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

#    dependencies = [
#        ('dcim', '0052_virtual_chassis'),
#    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='inventoryitem',
            field=models.ForeignKey(blank=True, help_text='Optionally link this interface to an inventory itme', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventoryitem', to='dcim.InventoryItem'),
        ),
    ]
