from django.db import models, connection


class SiteManager(models.Manager):

    def averages_join(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT sites_site.id,
            sites_site.name,
            AVG(sites_sitedetail.a) AS avg_a,
            AVG(sites_sitedetail.b) AS avg_b
            FROM sites_site
            LEFT OUTER JOIN sites_sitedetail
            ON ( sites_site.id = sites_sitedetail.site_id )
            GROUP BY sites_site.id, sites_site.name
            ORDER BY sites_site.name ASC;
        """)

        results = []
        for row in cursor.fetchall():
            site = self.model(id=row[0], name=row[1])
            site.avg_a = row[2]
            site.avg_b = row[3]
            results.append(site)
        return results


class Site(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()

    average_objects = SiteManager()

    def __str__(self):
        return self.name


class SiteDetail(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    a = models.DecimalField(max_digits=4, decimal_places=2)
    b = models.DecimalField(max_digits=4, decimal_places=2)