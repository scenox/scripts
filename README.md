# scripts

## helm-teams-watchdog.py
This Python script checks a [helm](https://github.com/helm/helm) chart repository every 10 minutes for new releases and sends a POST MessageCard to a Microsoft Teams channel webhook URL if a new release appears, using the 'created' timestamp in the helm index.yaml file compared with current time.

Create cronjob to run this script every 10 mins in Linux:
```
crontab -e
*/10 * * * * python3 helm-teams-watchdog.py
```
