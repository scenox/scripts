# scripts

## helm-teams-watchdog.py
This Python script checks a [helm](https://github.com/helm/helm) chart repository every 10 minutes for new releases and sends a POST request to a Microsoft Teams channel via webhook if a new release appears, using the helm 'created' timestamp.

Create cronjob to run this script every 10 mins in Linux:
```
crontab -e
*/10 * * * * python3 helm-teams-watchdog.py
```
