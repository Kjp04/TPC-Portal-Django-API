# Generated by Django 3.2.8 on 2022-03-12 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=10, null=True)),
                ('github', models.CharField(max_length=50, null=True)),
                ('linkedin', models.CharField(max_length=50, null=True)),
                ('no_of_offers', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(default=None, upload_to='studentPhoto')),
                ('department', models.CharField(max_length=50, null=True)),
                ('batch', models.IntegerField(null=True)),
                ('rait_email', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_one', models.ImageField(default=None, upload_to='certificate')),
                ('certificate_two', models.ImageField(default=None, upload_to='certificate')),
                ('certificate_three', models.ImageField(default=None, upload_to='certificate')),
                ('certificate_four', models.ImageField(default=None, upload_to='certificate')),
                ('acad_achievement_one', models.CharField(max_length=50, null=True)),
                ('acad_achievement_two', models.CharField(max_length=50, null=True)),
                ('acad_achievement_three', models.CharField(max_length=50, null=True)),
                ('acad_achievement_four', models.CharField(max_length=50, null=True)),
                ('career_obj', models.CharField(max_length=1000, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpc_api.student')),
            ],
            options={
                'verbose_name_plural': 'Student SkillSet',
            },
        ),
        migrations.CreateModel(
            name='PlacementDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_letter_one', models.ImageField(default=None, upload_to='offerLetter')),
                ('offer_letter_two', models.ImageField(default=None, upload_to='offerLetter')),
                ('placed_org_one', models.CharField(max_length=50, null=True)),
                ('placed_org_two', models.CharField(max_length=50, null=True)),
                ('package_one', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('package_two', models.DecimalField(decimal_places=4, max_digits=12, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpc_api.student')),
            ],
            options={
                'verbose_name_plural': 'Student Placement Detail',
            },
        ),
        migrations.CreateModel(
            name='OtherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies', models.CharField(max_length=1000, null=True)),
                ('pos_of_res_one', models.CharField(max_length=50, null=True)),
                ('pos_of_res_two', models.CharField(max_length=50, null=True)),
                ('pos_of_res_three', models.CharField(max_length=50, null=True)),
                ('pos_of_res_four', models.CharField(max_length=50, null=True)),
                ('extracuricular_one', models.CharField(max_length=500, null=True)),
                ('extracuricular_two', models.CharField(max_length=500, null=True)),
                ('extracuricular_three', models.CharField(max_length=500, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpc_api.student')),
            ],
            options={
                'verbose_name_plural': 'Student Other Info',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_one', models.CharField(max_length=1000, null=True)),
                ('internship_two', models.CharField(max_length=1000, null=True)),
                ('internship_three', models.CharField(max_length=1000, null=True)),
                ('project_one', models.CharField(max_length=1000, null=True)),
                ('project_two', models.CharField(max_length=1000, null=True)),
                ('project_three', models.CharField(max_length=1000, null=True)),
                ('pref_lang', models.CharField(max_length=50, null=True)),
                ('technologies', models.CharField(max_length=1000, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpc_api.student')),
            ],
            options={
                'verbose_name_plural': 'Student Experience',
            },
        ),
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenth_percent', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('twelveth_percent', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem1_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem2_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem3_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem4_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem5_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem6_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem7_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sem8_pointer', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('be_percent', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpc_api.student')),
            ],
            options={
                'verbose_name_plural': 'Student Academic Info',
            },
        ),
    ]
