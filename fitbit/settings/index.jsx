
function settingsComponent(props) {
  return (
    <Page>
      <Text><Text bold>Last file forwarded: </Text>{props.settingsStorage.getItem('fileNbr')}</Text>
      <Text><Text bold>Last status: </Text>{props.settingsStorage.getItem('status')}</Text>
    </Page>
  );
}

registerSettingsPage(settingsComponent)