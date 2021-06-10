# Generated by Django 2.2.16 on 2021-06-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0147_validate_ee_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorysource',
            name='source',
            field=models.CharField(
                choices=[
                    ('file', 'File, Directory or Script'),
                    ('scm', 'Sourced from a Project'),
                    ('ec2', 'Amazon EC2'),
                    ('gce', 'Google Compute Engine'),
                    ('azure_rm', 'Microsoft Azure Resource Manager'),
                    ('vmware', 'VMware vCenter'),
                    ('satellite6', 'Red Hat Satellite 6'),
                    ('openstack', 'OpenStack'),
                    ('rhv', 'Red Hat Virtualization'),
                    ('tower', 'Red Hat Ansible Automation Platform'),
                    ('insights', 'Red Hat Insights'),
                ],
                default=None,
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name='inventoryupdate',
            name='source',
            field=models.CharField(
                choices=[
                    ('file', 'File, Directory or Script'),
                    ('scm', 'Sourced from a Project'),
                    ('ec2', 'Amazon EC2'),
                    ('gce', 'Google Compute Engine'),
                    ('azure_rm', 'Microsoft Azure Resource Manager'),
                    ('vmware', 'VMware vCenter'),
                    ('satellite6', 'Red Hat Satellite 6'),
                    ('openstack', 'OpenStack'),
                    ('rhv', 'Red Hat Virtualization'),
                    ('tower', 'Red Hat Ansible Automation Platform'),
                    ('insights', 'Red Hat Insights'),
                ],
                default=None,
                max_length=32,
            ),
        ),
    ]
