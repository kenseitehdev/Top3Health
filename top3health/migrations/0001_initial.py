# Generated by Django 5.1.5 on 2025-03-02 21:58

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=14, unique=True)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('Height_ft', models.IntegerField(null=True)),
                ('Height_in', models.IntegerField(null=True)),
                ('Weight_in_pounds', models.IntegerField(null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('role', models.CharField(choices=[('dietician', 'Dietician'), ('director', 'Director'), ('custom_admin', 'Custom_admin'), ('user', 'User')], default='user', max_length=20)),
                ('mode', models.CharField(blank=True, choices=[('regular', 'Regular'), ('study_mode', 'Study_mode')], default='regular', max_length=10)),
                ('study_type', models.CharField(blank=True, choices=[('diabetes', 'Diabetes'), ('cvd', 'Cvd')], max_length=10)),
                ('middle_initial', models.CharField(blank=True, max_length=1, null=True)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(blank=True, max_length=30, null=True)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('dob', models.CharField(max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Measure', models.CharField(blank=True, max_length=10, null=True)),
                ('Weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Unit', models.CharField(blank=True, max_length=10, null=True)),
                ('Prep', models.CharField(blank=True, max_length=10, null=True)),
                ('GI', models.CharField(blank=True, max_length=10, null=True)),
                ('Water', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Water_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Energy', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Energy_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Protein', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Protein_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Total_lipid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Total_lipid_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Carbs', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Carbs_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fiber', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fiber_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Sugars', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Sugars_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Boron', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Boron_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Calcium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Calcium_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Chloride', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Chloride_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Chromium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Chromium_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Copper', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Copper_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fluoride', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fluoride_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Iodine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Iodine_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Iron', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Iron_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Magnesium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Magnesium_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Manganese', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Manganese_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Molybdenum', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Molybdenum_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Phosphorus', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Phosphorus_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Potassium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Potassium_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Selenium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Selenium_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Sodium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Sodium_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Zinc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Zinc_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Thiamin_B1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Thiamin_B1_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Riboflavin_B2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Riboflavin_B2_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Niacin_B3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Niacin_B3_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_B6', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_B6_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_B12', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_B12_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Biotin_B7', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Biotin_B7_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Choline', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Choline_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Folate_B9', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Folate_B9_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Pantothenic', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Pantothenic_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_C', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_C_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_A_RAE', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_A_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_D_IU', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_D_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_E_ATE', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_E_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_K', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Vitamin_K_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_total_sat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_sat_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_total_mono', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_mono_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_total_poly', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_poly_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_total_trans', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Fatty_acids_trans_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Cholesterol', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Cholesterol_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Omega_3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Omega_3_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Omega_6', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Omega_6_DV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dietician_note',
            fields=[
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('note1', models.CharField(blank=True, max_length=50, null=True)),
                ('note2', models.CharField(blank=True, max_length=50, null=True)),
                ('note3', models.CharField(blank=True, max_length=50, null=True)),
                ('note4', models.CharField(blank=True, max_length=50, null=True)),
                ('note5', models.CharField(blank=True, max_length=50, null=True)),
                ('note6', models.CharField(blank=True, max_length=50, null=True)),
                ('note7', models.CharField(blank=True, max_length=50, null=True)),
                ('note8', models.CharField(blank=True, max_length=50, null=True)),
                ('note9', models.CharField(blank=True, max_length=50, null=True)),
                ('note10', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myallergicfoods',
            fields=[
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('allergicFood1', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood2', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood3', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood4', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood5', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood6', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood7', models.CharField(blank=True, max_length=16, null=True)),
                ('allergicFood8', models.CharField(blank=True, max_length=16, null=True)),
                ('Food_substitute_1', models.CharField(blank=True, max_length=16, null=True)),
                ('Food_substitute_2', models.CharField(blank=True, max_length=16, null=True)),
                ('Food_substitute_3', models.CharField(blank=True, max_length=16, null=True)),
                ('Food_substitute_4', models.CharField(blank=True, max_length=16, null=True)),
                ('Food_substitute_5', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myexpenses',
            fields=[
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('family_eatout_count', models.IntegerField(blank=True, null=True)),
                ('weekly_eatout_cost', models.IntegerField(blank=True, null=True)),
                ('family_grocery_count', models.IntegerField(blank=True, null=True)),
                ('weekly_grocery_cost', models.IntegerField(blank=True, null=True)),
                ('Misc_expense_member', models.IntegerField(blank=True, null=True)),
                ('Misc_expenses', models.IntegerField(blank=True, null=True)),
                ('family_premium_count', models.IntegerField(blank=True, null=True)),
                ('insurance_premium', models.IntegerField(blank=True, null=True)),
                ('members_for_office_visit', models.IntegerField(blank=True, null=True)),
                ('office_visit_cost', models.IntegerField(blank=True, null=True)),
                ('members_for_prescriptions', models.IntegerField(blank=True, null=True)),
                ('prescription_cost', models.IntegerField(blank=True, null=True)),
                ('members_for_oop', models.IntegerField(blank=True, null=True)),
                ('oop_cost', models.IntegerField(blank=True, null=True)),
                ('members_for_gym', models.IntegerField(blank=True, null=True)),
                ('gym_cost', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myfitness',
            fields=[
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('moderate_intensity', models.IntegerField(blank=True, default=0, null=True)),
                ('vigorous_intensity', models.IntegerField(blank=True, default=0, null=True)),
                ('muscle_build', models.IntegerField(blank=True, default=0, null=True)),
                ('balance', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myfoodgroups',
            fields=[
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='myfoodgroups', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('All_veggies', models.IntegerField()),
                ('Beans_Lentils', models.IntegerField()),
                ('Fruits_Berries', models.IntegerField()),
                ('Protein', models.IntegerField()),
                ('Dairy', models.IntegerField()),
                ('Grains', models.IntegerField()),
                ('Allergic1', models.CharField(blank=True, max_length=30, null=True)),
                ('Substitute1', models.CharField(blank=True, max_length=30, null=True)),
                ('Allergic2', models.CharField(blank=True, max_length=30, null=True)),
                ('Substitute2', models.CharField(blank=True, max_length=30, null=True)),
                ('Allergic3', models.CharField(blank=True, max_length=30, null=True)),
                ('Substitute3', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myfoodsuggestions',
            fields=[
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Salads', models.CharField(max_length=16)),
                ('Sandwiches', models.CharField(max_length=16)),
                ('Fruits_Berries', models.CharField(max_length=16)),
                ('Dairy', models.CharField(max_length=16)),
                ('Pasta', models.CharField(max_length=16)),
                ('Egg_based', models.CharField(max_length=16)),
                ('Grains', models.CharField(max_length=16)),
                ('Soups', models.CharField(max_length=16)),
                ('Oats', models.CharField(max_length=16)),
                ('Beans_Legumes', models.CharField(max_length=16)),
                ('Smoothies', models.CharField(max_length=16)),
                ('Tacos_Burritos', models.CharField(max_length=16)),
                ('Nuts_Seeds', models.CharField(max_length=16)),
                ('Roti', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Beginpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('begin_date', models.DateField(blank=True, max_length=10, null=True)),
                ('daily_log_time', models.TimeField(blank=True, null=True)),
                ('weekly_log_time', models.TimeField(blank=True, null=True)),
                ('weekly_suggestion_time', models.TimeField(blank=True, null=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dietician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Healthsym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Minor1', models.CharField(blank=True, max_length=30, null=True)),
                ('Minor2', models.CharField(blank=True, max_length=30, null=True)),
                ('Minor3', models.CharField(blank=True, max_length=30, null=True)),
                ('Minor4', models.CharField(blank=True, max_length=30, null=True)),
                ('Minor5', models.CharField(blank=True, max_length=40, null=True)),
                ('Major1', models.CharField(blank=True, max_length=20, null=True)),
                ('Major2', models.CharField(blank=True, max_length=20, null=True)),
                ('Major3', models.CharField(blank=True, max_length=20, null=True)),
                ('Major4', models.CharField(blank=True, max_length=30, null=True)),
                ('Major5', models.CharField(blank=True, max_length=30, null=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mydailylog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veggies', models.IntegerField()),
                ('beans_lentils', models.IntegerField()),
                ('fruits_berries', models.IntegerField()),
                ('dairy', models.IntegerField()),
                ('grains', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('moderate_intensity', models.IntegerField()),
                ('vigorous_intensity', models.IntegerField()),
                ('muscle_build', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('Stretches', models.CharField(blank=True, max_length=50, null=True)),
                ('Stretch_check', models.BooleanField(default=False)),
                ('Reduce_processed', models.CharField(blank=True, max_length=50, null=True)),
                ('Reduce_processed_check', models.BooleanField(default=False)),
                ('Prepare_meals', models.CharField(blank=True, max_length=50, null=True)),
                ('Prepare_meals_check', models.BooleanField(default=False)),
                ('Wake_time', models.CharField(blank=True, max_length=50, null=True)),
                ('Wake_time_check', models.BooleanField(default=False)),
                ('food_cost_savings', models.CharField(blank=True, max_length=50, null=True)),
                ('food_savings_check', models.BooleanField(default=False)),
                ('Clear_kitchen', models.CharField(blank=True, max_length=50, null=True)),
                ('Clear_kitchen_check', models.BooleanField(default=False)),
                ('Brush_Floss', models.CharField(blank=True, max_length=50, null=True)),
                ('Brush_Floss_check', models.BooleanField(default=False)),
                ('Groceries_shop', models.CharField(blank=True, max_length=30, null=True)),
                ('Groceries_shop_check', models.BooleanField(default=False)),
                ('daily_mindfulness', models.CharField(blank=True, max_length=50, null=True)),
                ('daily_mindfulness_check', models.BooleanField(default=False)),
                ('food_suggestions', models.CharField(blank=True, max_length=50, null=True)),
                ('food_suggestions_check', models.BooleanField(default=False)),
                ('reduce_alcohol', models.CharField(blank=True, max_length=50, null=True)),
                ('reduce_alcohol_check', models.BooleanField(default=False)),
                ('reduce_smoking', models.CharField(blank=True, max_length=50, null=True)),
                ('reduce_smoking_check', models.BooleanField(default=False)),
                ('custom_habit_1', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_habit_1_check', models.BooleanField(default=False)),
                ('custom_habit_2', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_habit_2_check', models.BooleanField(default=False)),
                ('custom_habit_3', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_habit_3_check', models.BooleanField(default=False)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Myhabits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Stretches', models.CharField(blank=True, max_length=50, null=True)),
                ('Reduce_processed', models.CharField(blank=True, max_length=50, null=True)),
                ('Prepare_meals', models.CharField(blank=True, max_length=50, null=True)),
                ('Wake_time', models.CharField(blank=True, max_length=50, null=True)),
                ('food_cost_savings', models.CharField(blank=True, max_length=50, null=True)),
                ('Clear_kitchen', models.CharField(blank=True, max_length=50, null=True)),
                ('Brush_Floss', models.CharField(blank=True, max_length=50, null=True)),
                ('Groceries_shop', models.CharField(blank=True, max_length=30, null=True)),
                ('daily_mindfulness', models.CharField(blank=True, max_length=50, null=True)),
                ('food_suggestions', models.CharField(blank=True, max_length=50, null=True)),
                ('reduce_alcohol', models.CharField(blank=True, max_length=50, null=True)),
                ('reduce_smoking', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_habit_1', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_habit_2', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_habit_3', models.CharField(blank=True, max_length=50, null=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myhabits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Myhealthscreening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Blood_glucose', models.CharField(blank=True, max_length=4, null=True)),
                ('A1C', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('BP_systolic', models.IntegerField(blank=True, default=None, null=True)),
                ('BP_diastolic', models.IntegerField(blank=True, default=None, null=True)),
                ('Total_Cholesterol', models.IntegerField(blank=True, default=None, null=True)),
                ('HDL', models.IntegerField(blank=True, default=None, null=True)),
                ('LDL', models.IntegerField(blank=True, default=None, null=True)),
                ('Triglycerides', models.IntegerField(blank=True, default=None, null=True)),
                ('Smoker', models.CharField(blank=True, default=None, max_length=3, null=True)),
                ('Blood_type', models.CharField(blank=True, default=None, max_length=3, null=True)),
                ('Dental_checkups', models.BooleanField(default=False)),
                ('Dental_cleanings', models.BooleanField(default=False)),
                ('Vision_checkups', models.BooleanField(default=False)),
                ('Screen_date', models.DateField(blank=True, max_length=10, null=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mytypmeals1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('BCuisine1', models.CharField(blank=True, max_length=50, null=True)),
                ('B1_freq', models.CharField(blank=True, max_length=16, null=True)),
                ('Breakfast1', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB11', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB12', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB13', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB14', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB15', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB16', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB17', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientB18', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientbdr11', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientbdr12', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientbdr13', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientbdr14', models.CharField(blank=True, max_length=50, null=True)),
                ('LCuisine1', models.CharField(blank=True, max_length=50, null=True)),
                ('L1_freq', models.CharField(blank=True, max_length=16, null=True)),
                ('Lunch1', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL11', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL12', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL13', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL14', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL15', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL16', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL17', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientL18', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientldr11', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientldr12', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientldr13', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientldr14', models.CharField(blank=True, max_length=50, null=True)),
                ('DCuisine1', models.CharField(blank=True, max_length=50, null=True)),
                ('D1_freq', models.CharField(blank=True, max_length=16, null=True)),
                ('Dinner1', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD11', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD12', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD13', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD14', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD15', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD16', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD17', models.CharField(blank=True, max_length=50, null=True)),
                ('IngredientD18', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientddr11', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientddr12', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientddr13', models.CharField(blank=True, max_length=50, null=True)),
                ('Ingredientddr14', models.CharField(blank=True, max_length=50, null=True)),
                ('Snack1', models.CharField(blank=True, max_length=50, null=True)),
                ('Snack1_freq', models.CharField(blank=True, max_length=16, null=True)),
                ('Snack2', models.CharField(blank=True, max_length=50, null=True)),
                ('Snack2_freq', models.CharField(blank=True, max_length=16, null=True)),
                ('Water_intake', models.CharField(blank=True, max_length=50, null=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_topic', models.CharField(blank=True, choices=[('diabetes', 'Diabetes'), ('cardiovascular', 'Cardiovascular')], max_length=20, null=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Supplement_1', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Supplement_2', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Supplement_3', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Supplement_4', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Supplement_5', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
